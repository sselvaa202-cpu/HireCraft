# HireCraft - LLM Client

import httpx

from app.ai.config import ai_settings
from app.ai.provider import LLMProvider


class LLMClient(LLMProvider):
    """
    Generic OpenAI-compatible LLM client.
    """

    def __init__(self):
        self.api_key = ai_settings.llm_api_key
        self.base_url = ai_settings.llm_base_url
        self.model = ai_settings.llm_model

    def is_configured(self) -> bool:
        """
        Check whether the LLM is properly configured.
        """

        return bool(
            self.api_key
            and self.base_url
            and self.model
        )

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to the configured LLM.
        """

        if not self.is_configured():
            raise RuntimeError(
                "LLM is not configured. "
                "Please configure LLM_API_KEY, "
                "LLM_BASE_URL and LLM_MODEL."
            )

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        response = httpx.post(
            self.base_url,
            headers=headers,
            json=payload,
            timeout=60.0,
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]


llm_client = LLMClient()