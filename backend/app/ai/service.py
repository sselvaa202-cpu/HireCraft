# HireCraft - Centralized AI Service

import json

from app.ai.client import llm_client
from app.ai.errors import AIRequestError


class AIService:
    """
    Centralized service for all AI operations in HireCraft.

    All future AI modules such as:
    - LinkedIn
    - GitHub
    - Projects
    - Interview
    will use this service instead of calling the LLM directly.
    """

    def __init__(self, client=llm_client):
        self.client = client

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to the configured LLM
        and return the raw response.
        """

        if not prompt or not prompt.strip():
            raise AIRequestError(
                "AI prompt cannot be empty."
            )

        return self.client.generate(prompt)

    def generate_json(self, prompt: str) -> dict:
        """
        Generate a response from the LLM
        and convert it into a Python dictionary.
        """

        response = self.generate(prompt)

        try:
            return json.loads(response)

        except json.JSONDecodeError as e:
            raise AIRequestError(
                "LLM returned invalid JSON."
            ) from e


ai_service = AIService()