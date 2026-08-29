# HireCraft - Centralized AI Service

from typing import Type, TypeVar

from pydantic import BaseModel

from app.ai.client import llm_client
from app.ai.retry import retry_ai_request
from app.ai.validators import parse_json_response


T = TypeVar("T", bound=BaseModel)


class AIService:
    """
    Centralized AI service for HireCraft.

    Responsibilities:
    - Send prompts to the configured LLM
    - Parse JSON responses
    - Validate responses using Pydantic
    - Retry temporary AI failures
    """

    def __init__(self):
        self.client = llm_client

    def generate_structured(
        self,
        prompt: str,
        response_model: Type[T],
    ) -> T:
        """
        Generate and validate a structured AI response.
        """

        # Send request to LLM with retry support
        raw_response = retry_ai_request(
            lambda: self.client.generate(prompt)
        )

        # Parse JSON response
        parsed_response = parse_json_response(
            raw_response
        )

        # Validate against Pydantic schema
        validated_response = response_model.model_validate(
            parsed_response
        )

        return validated_response


ai_service = AIService()