"""Tests for the orchestrator API."""

from fastapi.testclient import TestClient

from agentic_sdlc_orchestrator.api import app


def test_health_check() -> None:
    """The health endpoint should report that the service is operational."""
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}