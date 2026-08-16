"""Validated data contracts for software change requests."""

from enum import StrEnum
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ChangePriority(StrEnum):
    """Supported priority levels for a software change."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ChangeRequest(BaseModel):
    """A validated request submitted to the agentic workflow."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    title: str = Field(min_length=5, max_length=120)
    description: str = Field(min_length=20, max_length=5_000)
    repository: str = Field(min_length=3, max_length=200)
    acceptance_criteria: list[str] = Field(min_length=1, max_length=10)
    priority: ChangePriority = ChangePriority.MEDIUM


class ChangeRequestReceipt(BaseModel):
    """Acknowledgement returned when a change request is accepted."""

    model_config = ConfigDict(extra="forbid")

    request_id: UUID
    status: Literal["accepted"] = "accepted"
    change_request: ChangeRequest