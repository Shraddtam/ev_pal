"""Request-scoped observability context and response-header helpers."""
from contextvars import ContextVar, Token
from uuid import uuid4

request_id_var: ContextVar[str] = ContextVar("request_id", default="system")
session_hash_var: ContextVar[str] = ContextVar("session_hash", default="anonymous")

def request_context() -> dict[str, str]:
    return {"request_id": request_id_var.get(), "session_id_hash": session_hash_var.get()}

def resolve_request_id(incoming_request_id: str | None) -> str:
    """Keep a supplied correlation ID or create one at the application edge."""
    return incoming_request_id.strip() if incoming_request_id and incoming_request_id.strip() else str(uuid4())

def bind_request_context(request_id: str, session_id_hash: str) -> tuple[Token, Token]:
    return request_id_var.set(request_id), session_hash_var.set(session_id_hash)

def reset_request_context(tokens: tuple[Token, Token]) -> None:
    request_id_var.reset(tokens[0])
    session_hash_var.reset(tokens[1])

def apply_observability_headers(response, request_id: str, app_version: str):
    response.headers["X-Request-ID"] = request_id
    response.headers["X-App-Version"] = app_version
    return response
