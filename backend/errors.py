class EVPalError(Exception):
    error_code = "EVPAL_ERROR"
    status_code = 400
    def __init__(self, message: str, details: dict | None = None):
        super().__init__(message)
        self.details = details or {}

class ValidationError(EVPalError): error_code = "VALIDATION_ERROR"
class DataNotFound(EVPalError): error_code = "DATA_NOT_FOUND"; status_code = 404
class SourceUnverified(EVPalError): error_code = "SOURCE_UNVERIFIED"; status_code = 409
class ModelUnavailable(EVPalError): error_code = "MODEL_UNAVAILABLE"; status_code = 503
class RAGInsufficientEvidence(EVPalError): error_code = "RAG_INSUFFICIENT_EVIDENCE"; status_code = 422
class ToolExecutionError(EVPalError): error_code = "TOOL_EXECUTION_ERROR"; status_code = 502
