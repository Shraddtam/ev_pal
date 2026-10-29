from pathlib import Path
from datetime import date
from time import perf_counter
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from backend.services import battery_health, charging, dashboard, market, policies, recommendations, tco, vehicles
from backend.errors import EVPalError
from backend.observability.context import apply_observability_headers, bind_request_context, request_id_var, reset_request_context, resolve_request_id
from backend.observability.logging import APP_VERSION, configure_logging, log_event
from backend.observability.metrics import record_request, render_metrics
from backend.observability.redaction import hash_identifier, redact

app=FastAPI(title="EV PAL API",version=APP_VERSION,description="Vehicle catalogue entries link to official manufacturer material; other services declare their verification status.")

@app.on_event("startup")
async def startup() -> None:
    configure_logging()
    log_event("app", "application_started", "EV PAL application started", app_version=APP_VERSION)

@app.on_event("shutdown")
async def shutdown() -> None:
    log_event("app", "application_stopped", "EV PAL application stopped")

@app.middleware("http")
async def request_observability(request: Request, call_next):
    request_id = resolve_request_id(request.headers.get("X-Request-ID"))
    context_tokens = bind_request_context(request_id, hash_identifier(request.headers.get("X-Session-ID")))
    started = perf_counter()
    try:
        response = await call_next(request)
    except Exception:
        raise
    finally:
        duration_ms = round((perf_counter() - started) * 1000, 2)
    apply_observability_headers(response, request_id, APP_VERSION)
    size = response.headers.get("content-length", "0")
    record_request(request.url.path, response.status_code, duration_ms)
    log_event("access", "request_completed", "HTTP request completed", method=request.method, path=request.url.path, status_code=response.status_code, duration_ms=duration_ms, response_bytes=size, data={"client_type": request.headers.get("user-agent", "unknown")[:120]})
    reset_request_context(context_tokens)
    return response

@app.exception_handler(EVPalError)
async def evpal_error_handler(request: Request, exc: EVPalError):
    request_id = request_id_var.get()
    log_event("error", "domain_error", str(exc), level=30, data={"error_code": exc.error_code, "module": request.url.path})
    body = {"error_code": exc.error_code, "message": str(exc), "request_id": request_id}
    if __import__("os").getenv("APP_ENV", "development") == "development": body["details"] = redact(exc.details)
    return JSONResponse(body, status_code=exc.status_code, headers={"X-Request-ID": request_id})

@app.exception_handler(Exception)
async def unexpected_error_handler(request: Request, exc: Exception):
    request_id = request_id_var.get()
    log_event("error", "unhandled_exception", "Unhandled application exception", level=40, data={"module": request.url.path, "error_type": type(exc).__name__}, exc_info=True)
    body = {"error_code": "INTERNAL_ERROR", "message": "Something went wrong. Please provide the request ID to support.", "request_id": request_id}
    if __import__("os").getenv("APP_ENV", "development") == "development": body["details"] = {"type": type(exc).__name__}
    return JSONResponse(body, status_code=500, headers={"X-Request-ID": request_id})

@app.get('/api/health')
def health(): return {"status":"ok","version":APP_VERSION,"vehicle_catalogue":"official_manufacturer_sources","other_data_status":"demo_not_verified"}
@app.get('/ready')
def ready(): return {"status":"ready","checks":{"catalogue":"loaded","csv_data_access":"available","ml_model":"development_heuristic","rag":"not_configured","database":"not_configured"}}
@app.get('/metrics', response_class=PlainTextResponse)
def metrics(): return render_metrics()
@app.get('/api/dashboard')
def get_dashboard(): return dashboard.summary()
@app.get('/api/vehicles')
def get_vehicles(query:str="",manufacturer:str="",body_type:str="",chemistry:str="",min_price:float=0,max_price:float=1e12,min_range:float=0,sort:str="price"): return vehicles.search(query,manufacturer,body_type,chemistry,min_price,max_price,min_range,sort)
@app.get('/api/vehicles/{vehicle_id}')
def get_vehicle(vehicle_id:str):
    item=vehicles.detail(vehicle_id)
    if not item: raise HTTPException(404,"Vehicle not found")
    return item
@app.post('/api/recommendations')
def get_recommendations(payload:dict): return recommendations.recommend(payload)
@app.post('/api/battery-health/estimate')
def battery_estimate(payload:dict): return battery_health.estimate(payload)
@app.post('/api/tco/calculate')
def tco_calculate(payload:dict): return tco.calculate(payload)
@app.get('/api/policies')
def get_policies(query:str="",state:str="",status:str="",category:str=""): return policies.list_policies(query,state,status)
@app.post('/api/policies/ask')
def policy_ask(payload:dict): return policies.ask(payload.get('question',''))
@app.get('/api/charging/stations')
def get_stations(city:str="",state:str="",charger_type:str="",operator:str=""): return charging.stations(city,state,charger_type,operator)
@app.get('/api/market')
def get_market(state:str="",manufacturer:str="",vehicle_id:str=""): return market.insights(state,manufacturer,vehicle_id)
@app.post('/api/client-logs', status_code=202)
def receive_client_logs(payload: dict):
    events = payload.get("events", [])[:20] if isinstance(payload, dict) else []
    log_event("client", "browser_events_received", "Browser events received", data={"event_count": len(events), "events": redact(events)})
    return {"accepted": len(events), "request_id": request_id_var.get()}
@app.get('/api/admin/logs')
def read_logs(category: str = "app", request_id: str = "", level: str = "", search: str = "", date_from: str = "", date_to: str = "", limit: int = 100):
    if category not in {"all", "app", "access", "error", "audit", "ingestion", "ml", "rag", "agent", "security", "client"}:
        log_event("security", "invalid_log_category", "Invalid admin log category requested", level=30, data={"category": category})
        return JSONResponse({"error_code":"VALIDATION_ERROR","message":"Unknown log category","request_id":request_id_var.get()}, status_code=400)
    log_dir = Path(__import__("os").getenv("LOG_DIR", Path(__file__).resolve().parents[1] / "logs"))
    paths = list(log_dir.glob("*.log")) if category == "all" else [log_dir / f"{category}.log"]
    entries=[]
    for path in paths:
        if not path.exists(): continue
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()[-max(1, min(limit, 500)):]:
            try: entry = __import__("json").loads(line)
            except __import__("json").JSONDecodeError: continue
            if request_id and entry.get("request_id") != request_id: continue
            if level and entry.get("level") != level.upper(): continue
            if date_from and str(entry.get("timestamp", ""))[:10] < date_from: continue
            if date_to and str(entry.get("timestamp", ""))[:10] > date_to: continue
            if search and search.lower() not in __import__("json").dumps(entry).lower(): continue
            entries.append(redact(entry))
    log_event("audit", "admin_logs_viewed", "Admin log view queried", data={"category":category,"request_id_filter":request_id or None,"result_count":len(entries)})
    return {"entries": entries[-max(1,min(limit,500)):], "request_id": request_id_var.get()}

@app.get('/api/admin/data-quality')
def data_quality():
    rows = vehicles.catalog()
    expected = ("manufacturer", "model", "variant", "body_type", "claimed_range_km", "battery")
    missing_core = [row["vehicle_id"] for row in rows if any(row.get(field) is None for field in expected)]
    official_sources = [row for row in rows if row.get("source", {}).get("source_type") == "official_manufacturer" and row.get("source", {}).get("source_url")]
    result = {
        "catalogue_rows": len(rows),
        "official_source_rows": len(official_sources),
        "missing_core_value_rows": missing_core,
        "duplicate_vehicle_ids": len(rows) - len({row["vehicle_id"] for row in rows}),
        "field_level_provenance": "not_yet_migrated",
        "schema_status": "legacy catalogue records; field-level value/unit/source metadata is scheduled for Phase 2 after schema approval",
    }
    log_event("audit", "data_quality_viewed", "Catalogue data-quality report generated", data=result)
    return result

@app.get('/api/admin/freshness')
def freshness():
    today = date.today()
    sources = []
    for row in vehicles.catalog():
        source = row.get("source", {})
        checked = source.get("last_checked")
        try: age_days = (today - date.fromisoformat(checked)).days if checked else None
        except ValueError: age_days = None
        sources.append({"vehicle_id":row["vehicle_id"],"vehicle":f'{row["manufacturer"]} {row["model"]} {row["variant"]}',"last_checked":checked,"age_days":age_days,"freshness":"fresh" if age_days is not None and age_days <= 90 else "needs_review","source_url":source.get("source_url"),"verified":source.get("source_type") == "official_manufacturer"})
    log_event("audit", "data_freshness_viewed", "Catalogue data-freshness report generated", data={"source_count":len(sources)})
    return {"stale_after_days":90,"sources":sources}

@app.get('/api/admin/system-health')
def system_health():
    checks = {"api":"available","catalogue":f"{len(vehicles.catalog())} source-linked variants loaded","csv_data_access":"available","model":"development heuristic only","rag":"not configured","database":"not configured"}
    return {"status":"ready","checks":checks,"request_id":request_id_var.get()}

STATIC=Path(__file__).resolve().parents[1]/'frontend'
@app.get('/')
def index(): return FileResponse(STATIC/'index.html')
app.mount('/static',StaticFiles(directory=STATIC),name='static')
