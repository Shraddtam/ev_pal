"""Structured, redacted, category-specific application logging."""
from __future__ import annotations
import gzip
import json
import logging
import os
import shutil
import sys
import time
from datetime import datetime, timezone, timedelta
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Any
from backend.observability.context import request_context
from backend.observability.redaction import redact

APP_VERSION = "0.3.0"
LOG_CATEGORIES = ("app", "access", "error", "audit", "ingestion", "ml", "rag", "agent", "security", "client")
_CONFIGURED = False

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "category": getattr(record, "category", "app"),
            "event": getattr(record, "event", "log"),
            "message": record.getMessage(),
            **request_context(),
            "app_version": APP_VERSION,
            "environment": os.getenv("APP_ENV", "development"),
        }
        for key in ("duration_ms", "status_code", "method", "path", "response_bytes", "data"):
            if hasattr(record, key):
                payload[key] = getattr(record, key)
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(redact(payload), default=str, ensure_ascii=False)

class HumanFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        ctx = request_context()
        return f"{datetime.now(timezone.utc).isoformat()} {record.levelname:<8} [{getattr(record, 'category', 'app')}] {getattr(record, 'event', 'log')} request_id={ctx['request_id']} {redact(record.getMessage())}"

class CategoryFilter(logging.Filter):
    def __init__(self, category: str):
        super().__init__()
        self.category = category
    def filter(self, record: logging.LogRecord) -> bool:
        return getattr(record, "category", "app") == self.category

class SizeAndTimeHandler(TimedRotatingFileHandler):
    """Daily rollover plus a conservative size rollover for development logs."""
    def __init__(self, filename: str, max_bytes: int, **kwargs: Any):
        super().__init__(filename, when="midnight", interval=1, backupCount=30, encoding="utf-8", utc=True, **kwargs)
        self.max_bytes = max_bytes

    def shouldRollover(self, record: logging.LogRecord) -> int:
        if super().shouldRollover(record):
            return 1
        if self.stream is None:
            self.stream = self._open()
        self.stream.seek(0, 2)
        return int(self.stream.tell() + len(self.format(record).encode("utf-8")) >= self.max_bytes)

    def doRollover(self) -> None:
        super().doRollover()
        for old in Path(self.baseFilename).parent.glob(Path(self.baseFilename).name + ".*"):
            if old.suffix == ".gz":
                continue
            try:
                with old.open("rb") as source, gzip.open(str(old) + ".gz", "wb") as target:
                    shutil.copyfileobj(source, target)
                old.unlink()
            except OSError:
                pass

def _cleanup(log_dir: Path, retention_days: int) -> None:
    cutoff = time.time() - timedelta(days=retention_days).total_seconds()
    for path in log_dir.glob("*.log.*.gz"):
        try:
            if path.stat().st_mtime < cutoff:
                path.unlink()
        except OSError:
            pass

def configure_logging() -> None:
    global _CONFIGURED
    if _CONFIGURED:
        return
    root = logging.getLogger("evpal")
    root.setLevel(getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper(), logging.INFO))
    root.propagate = False
    log_dir = Path(os.getenv("LOG_DIR", Path(__file__).resolve().parents[2] / "logs"))
    log_dir.mkdir(parents=True, exist_ok=True)
    max_bytes = int(float(os.getenv("LOG_MAX_MB", "5")) * 1024 * 1024)
    formatter = JsonFormatter()
    for category in LOG_CATEGORIES:
        handler = SizeAndTimeHandler(str(log_dir / f"{category}.log"), max_bytes=max_bytes)
        handler.setFormatter(formatter)
        handler.addFilter(CategoryFilter(category))
        root.addHandler(handler)
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter if os.getenv("LOG_FORMAT", "human").lower() == "json" else HumanFormatter())
    root.addHandler(console)
    _cleanup(log_dir, int(os.getenv("LOG_RETENTION_DAYS", "30")))
    _CONFIGURED = True

def log_event(category: str, event: str, message: str, *, level: int = logging.INFO, **fields: Any) -> None:
    """Write one structured event, preserving an optional exception traceback."""
    logger = logging.getLogger("evpal")
    exc_info = fields.pop("exc_info", None)
    logger.log(level, message, extra={"category": category, "event": event, **fields}, exc_info=exc_info)
