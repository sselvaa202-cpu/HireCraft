# HireCraft - AI Response Validators

import json

from pydantic import BaseModel, ValidationError

from app.ai.errors import AIRequestError


def parse_json_response(response: str) -> dict:
    """
    Convert an LLM response into a Python dictionary.
    """

    if not response or not response.strip():
        raise AIRequestError(
            "LLM returned an empty response."
        )

    cleaned_response = response.strip()

    # Remove markdown code fences if the LLM returns them
    if cleaned_response.startswith("```"):
        lines = cleaned_response.splitlines()

        # Remove opening ```json or ```
        if lines:
            lines = lines[1:]

        # Remove closing ```
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        cleaned_response = "\n".join(lines).strip()

    try:
        data = json.loads(cleaned_response)

    except json.JSONDecodeError as e:
        raise AIRequestError(
            "LLM returned invalid JSON."
        ) from e

    if not isinstance(data, dict):
        raise AIRequestError(
            "LLM response must be a JSON object."
        )

    return data


def validate_response(
    data: dict,
    response_model: type[BaseModel]
) -> BaseModel:
    """
    Validate AI-generated data using a Pydantic model.
    """

    try:
        return response_model.model_validate(data)

    except ValidationError as e:
        raise AIRequestError(
            f"AI response validation failed: {e}"
        ) from e