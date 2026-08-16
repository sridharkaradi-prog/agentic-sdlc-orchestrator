"""HTTP API for the Agentic SDLC Orchestrator."""

from fastapi import FastAPI

app = FastAPI(
    title="Agentic SDLC Orchestrator",
    description="Human-governed orchestration of software delivery workflows.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health_check() -> dict[str, str]:
    """Return the service health status."""
    return {"status": "ok"}