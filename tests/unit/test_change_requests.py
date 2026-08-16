"""Tests for the change-request API."""

from uuid import UUID

from fastapi.testclient import TestClient

from agentic_sdlc_orchestrator.api import app


def valid_change_request() -> dict[str, object]:
    """Return a valid software-change request payload."""
    return {
        "title": "Add audit logging",
        "description": (
            "Record every approved software change and the responsible user."
        ),
        "repository": "sridharkaradi-prog/agentic-sdlc-orchestrator",
        "acceptance_criteria": [
            "Every approved change has a request ID",
            "The responsible user is recorded",
        ],
        "priority": "high",
    }


def test_create_change_request_accepts_valid_input() -> None:
    """A valid request should be accepted and assigned an ID."""
    payload = valid_change_request()

    with TestClient(app) as client:
        response = client.post("/change-requests", json=payload)

    assert response.status_code == 202

    response_body = response.json()
    assert response_body["status"] == "accepted"
    assert response_body["change_request"] == payload

    UUID(response_body["request_id"])


def test_create_change_request_rejects_invalid_priority() -> None:
    """An unsupported priority should fail validation."""
    payload = valid_change_request()
    payload["priority"] = "urgent"

    with TestClient(app) as client:
        response = client.post("/change-requests", json=payload)

    assert response.status_code == 422

    validation_errors = response.json()["detail"]
    assert any(
        error["loc"][-1] == "priority"
        for error in validation_errors
    )