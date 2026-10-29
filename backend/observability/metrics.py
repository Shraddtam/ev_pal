"""Small dependency-free Prometheus exposition for the MVP."""
from __future__ import annotations
from collections import defaultdict
from threading import Lock

_lock = Lock()
_requests: dict[tuple[str, int], int] = defaultdict(int)
_latency: dict[str, list[float]] = defaultdict(list)
_errors: int = 0
_operation_latency: dict[str, list[float]] = defaultdict(list)

def record_request(path: str, status: int, duration_ms: float) -> None:
    global _errors
    with _lock:
        _requests[(path, status)] += 1
        _latency[path].append(duration_ms)
        if status >= 400:
            _errors += 1

def record_operation_latency(operation: str, duration_ms: float) -> None:
    with _lock:
        _operation_latency[operation].append(duration_ms)

def render_metrics() -> str:
    lines = ["# HELP evpal_requests_total HTTP requests handled", "# TYPE evpal_requests_total counter"]
    with _lock:
        for (path, status), count in _requests.items():
            lines.append(f'evpal_requests_total{{path="{path}",status="{status}"}} {count}')
        lines += ["# HELP evpal_request_latency_ms Request latency in milliseconds", "# TYPE evpal_request_latency_ms gauge"]
        for path, values in _latency.items():
            if values:
                lines.append(f'evpal_request_latency_ms{{path="{path}"}} {sum(values)/len(values):.2f}')
        lines += ["# HELP evpal_errors_total HTTP errors handled", "# TYPE evpal_errors_total counter", f"evpal_errors_total {_errors}"]
        lines += ["# HELP evpal_operation_latency_ms Service-operation latency in milliseconds", "# TYPE evpal_operation_latency_ms gauge"]
        for operation, values in _operation_latency.items():
            if values:
                lines.append(f'evpal_operation_latency_ms{{operation="{operation}"}} {sum(values)/len(values):.2f}')
    return "\n".join(lines) + "\n"
