"""HTTP API for the Agentic SDLC Orchestrator."""

from uuid import uuid4

from fastapi import FastAPI, status

from agentic_sdlc_orchestrator.models import (
    ChangeRequest,
    ChangeRequestReceipt,
)

app = FastAPI(
    title="Agentic SDLC Orchestrator",
    description="Human-governed orchestration of software delivery workflows.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Return the service health status."""
    return {"status": "ok"}


@app.post(
    "/change-requests",
    response_model=ChangeRequestReceipt,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["workflow"],
)
def create_change_request(
    change_request: ChangeRequest,
) -> ChangeRequestReceipt:
    """Validate and accept a software-change request."""
    return ChangeRequestReceipt(
        request_id=uuid4(),
        change_request=change_request,
    )