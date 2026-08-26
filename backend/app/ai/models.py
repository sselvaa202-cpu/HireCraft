# HireCraft - AI Response Models

from pydantic import BaseModel, Field


class AIResponse(BaseModel):
    """
    Standard response structure returned by HireCraft AI.
    """

    success: bool = True

    data: dict = Field(default_factory=dict)

    error: str | None = None