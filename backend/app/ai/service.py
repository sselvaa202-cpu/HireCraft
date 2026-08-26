# HireCraft - AI Service

from app.ai.client import llm_client
from app.ai.errors import AIConfigurationError, AIRequestError
from app.ai.prompts.job_analysis import build_job_analysis_prompt
from app.schemas.job import JobRequirement
from app.services.job_analysis import analyze_job_description


def analyze_job_with_ai(job_description: str) -> JobRequirement:
    """
    Analyze a job description using AI.

    If AI is unavailable or fails, fall back
    to the Phase 4 rule-based analyzer.
    """

    try:
        # Build the AI prompt
        prompt = build_job_analysis_prompt(
            job_description
        )

        # Ask the LLM for a response
        response = llm_client.generate(prompt)

        # Convert AI JSON response into JobRequirement
        return JobRequirement.model_validate_json(
            response
        )

    except (
        AIConfigurationError,
        AIRequestError,
        ValueError,
    ):
        # AI unavailable or invalid response.
        # Use the existing Phase 4 analyzer.
        return analyze_job_description(
            job_description
        )