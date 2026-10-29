import json
import logging
import unittest

from fastapi.responses import Response
from backend.observability.context import apply_observability_headers, request_id_var, resolve_request_id, session_hash_var
from backend.observability.logging import JsonFormatter
from backend.observability.redaction import redact


class RedactionTests(unittest.TestCase):
    def test_redacts_secrets_and_personal_data(self):
        result = redact({"api_key": "sk_verylongsecretvalue123", "email": "owner@example.com", "message": "Call +91 98765 43210"})
        self.assertEqual(result["api_key"], "[REDACTED]")
        self.assertEqual(result["email"], "[REDACTED]")
        self.assertIn("[REDACTED_PHONE]", result["message"])

    def test_preserves_operational_timestamp_and_hash(self):
        result = redact({"timestamp": "2026-10-30T19:20:24.388388+00:00", "session_id_hash": "cbac0c96abb1f7d3"})
        self.assertEqual(result["timestamp"], "2026-10-30T19:20:24.388388+00:00")
        self.assertEqual(result["session_id_hash"], "cbac0c96abb1f7d3")


class LogSchemaTests(unittest.TestCase):
    def test_json_log_has_required_observability_fields(self):
        token1 = request_id_var.set("schema-test-001")
        token2 = session_hash_var.set("hashed-session")
        try:
            record = logging.LogRecord("evpal", logging.INFO, __file__, 1, "safe message", (), None)
            record.category, record.event = "app", "schema_test"
            payload = json.loads(JsonFormatter().format(record))
        finally:
            request_id_var.reset(token1); session_hash_var.reset(token2)
        for key in ("timestamp", "level", "logger", "category", "event", "message", "request_id", "session_id_hash", "app_version", "environment"):
            self.assertIn(key, payload)
        self.assertEqual(payload["request_id"], "schema-test-001")


class RequestIdTests(unittest.TestCase):
    def test_request_id_is_propagated_to_response_headers(self):
        request_id = resolve_request_id("phase0-test-request")
        response = apply_observability_headers(Response("ok", media_type="text/plain"), request_id, "0.3.0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["x-request-id"], "phase0-test-request")
        self.assertEqual(response.headers["x-app-version"], "0.3.0")

    def test_blank_request_id_is_replaced(self):
        self.assertRegex(resolve_request_id("  "), r"^[0-9a-f-]{36}$")


if __name__ == "__main__":
    unittest.main()
