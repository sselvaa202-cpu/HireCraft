# HireCraft - AI Response Validation

from pydantic import ValidationError

from app.schemas.job import JobRequirement


def validate_job_analysis_response(
    data: dict
) -> JobRequirement:
    """
    Validate an AI-generated job analysis response.

    Converts the raw dictionary returned by the LLM
    into a validated JobRequirement object.
    """

    try:
        return JobRequirement.model_validate(data)

    except ValidationError as e:
        raise ValueError(
            f"Invalid AI job analysis response: {e}"
        )