# HireCraft - Centralized AI Service

from typing import TypeVar

from pydantic import BaseModel

from app.ai.client import llm_client
from app.ai.retry import retry_ai_request
from app.ai.validators import parse_json_response
from app.schemas.job import JobRequirement
from app.ai.prompts.job.analysis import build_job_analysis_prompt


T = TypeVar("T", bound=BaseModel)


class AIService:
    """
    Centralized AI service for HireCraft.

    Responsibilities:
    - Prompt handling
    - LLM communication
    - Retry handling
    - JSON parsing
    - Pydantic validation
    """

    def __init__(self):
        self.client = llm_client

    def generate_structured(
        self,
        prompt: str,
        response_model: type[T],
    ) -> T:
        """
        Generate a structured response from the LLM.
        """

        raw_response = retry_ai_request(
            lambda: self.client.generate(prompt)
        )

        parsed_response = parse_json_response(
            raw_response
        )

        validated_response = response_model.model_validate(
            parsed_response
        )

        return validated_response


def analyze_job_with_ai(
    job_description: str,
) -> JobRequirement:
    """
    Analyze a job description using the centralized AI service.
    """

    prompt = build_job_analysis_prompt(
        job_description
    )

    return ai_service.generate_structured(
        prompt=prompt,
        response_model=JobRequirement,
    )


ai_service = AIService()