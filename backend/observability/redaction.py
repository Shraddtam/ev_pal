"""Redact sensitive values before any data reaches a log formatter."""
from __future__ import annotations
import hashlib
import re
from typing import Any

SENSITIVE_KEY = re.compile(r"(api[_-]?key|authorization|cookie|password|secret|token|email|phone|session|user[_-]?id)", re.I)
EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE = re.compile(r"(?<!\d)(?:\+?\d[\d\s-]{8,}\d)(?!\d)")
TOKEN = re.compile(r"\b(?:sk|pk|eyJ)[A-Za-z0-9_\-]{16,}\b")

def hash_identifier(value: str | None) -> str:
    if not value:
        return "anonymous"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]

def redact_text(value: str) -> str:
    # ISO timestamps are operational metadata, not phone numbers.
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})", value):
        return value
    value = EMAIL.sub("[REDACTED_EMAIL]", value)
    value = PHONE.sub("[REDACTED_PHONE]", value)
    return TOKEN.sub("[REDACTED_TOKEN]", value)

def redact(value: Any, key: str | None = None) -> Any:
    if key == "session_id_hash":
        return value
    if key and SENSITIVE_KEY.search(key):
        return "[REDACTED]"
    if isinstance(value, str):
        return redact_text(value)
    if isinstance(value, dict):
        return {str(k): redact(v, str(k)) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [redact(item) for item in value]
    return value
