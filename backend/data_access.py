"""CSV data-access layer. Replace these readers with PostgreSQL repositories later."""
from __future__ import annotations
import csv
import hashlib
from functools import lru_cache
from pathlib import Path
from backend.observability.logging import log_event

DATA = Path(__file__).resolve().parents[1] / "data"

@lru_cache(maxsize=32)
def read_csv(relative_path: str) -> list[dict[str, str]]:
    path = DATA / relative_path
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    log_event("ingestion", "csv_loaded", "CSV data source loaded", data={"filename": path.name, "rows_accepted": len(rows), "rows_rejected": 0, "checksum": hashlib.sha256(path.read_bytes()).hexdigest(), "schema_version": "csv-v1"})
    return rows

def number(value, default=0.0) -> float:
    try: return float(value)
    except (TypeError, ValueError): return default

def clean(row: dict, fields: list[str]) -> dict:
    """Limit API records to UI-relevant columns without hiding synthetic provenance."""
    result = {field: row.get(field) for field in fields}
    result["source"] = {"label": "Synthetic / Prototype Data", "source_type": row.get("source_type", "synthetic"), "generated_at": row.get("generated_at"), "last_verified": row.get("last_verified")}
    return result
