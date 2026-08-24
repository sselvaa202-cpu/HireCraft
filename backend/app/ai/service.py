# HireCraft - AI Service

import json

from app.ai.client import llm_client
from app.ai.prompts.job_analysis import build_job_analysis_prompt
from app.ai.validation import validate_job_analysis_response
from app.schemas.job import JobRequirement


class AIService:
    """
    Main service responsible for AI-powered analysis.
    """

    def __init__(self):
        self.client = llm_client

    def analyze_job_description(
        self,
        job_description: str
    ) -> JobRequirement:
        """
        Analyze a job description using the LLM
        and return a validated JobRequirement object.
        """

        # Build prompt
        prompt = build_job_analysis_prompt(
            job_description
        )

        # Generate AI response
        response = self.client.generate(prompt)

        # Parse JSON
        try:
            data = json.loads(response)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"LLM returned invalid JSON: {e}"
            )

        # Validate AI response
        return validate_job_analysis_response(data)


ai_service = AIService()