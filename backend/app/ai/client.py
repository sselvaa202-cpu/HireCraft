# HireCraft - LLM Client

import httpx

from app.ai.config import ai_settings
from app.ai.errors import AIConfigurationError, AIRequestError
from app.ai.provider import LLMProvider
from app.ai.retry import retry_ai_request


class LLMClient(LLMProvider):
    """
    Generic OpenAI-compatible LLM client.

    Responsible for:
    - Checking LLM configuration
    - Sending requests to the LLM
    - Handling HTTP errors
    - Retrying temporary failures
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
        Generate an LLM response.

        Configuration errors fail immediately.

        Temporary request errors are handled
        by the retry mechanism.
        """

        # Configuration errors should not be retried.
        if not self.is_configured():
            raise AIConfigurationError(
                "LLM is not configured. "
                "Please configure LLM_API_KEY, "
                "LLM_BASE_URL and LLM_MODEL."
            )

        # Retry temporary LLM request failures.
        return retry_ai_request(
            lambda: self._make_request(prompt)
        )

    def _make_request(self, prompt: str) -> str:
        """
        Perform the actual HTTP request to the LLM.
        """

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

        try:
            response = httpx.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=60.0,
            )

            response.raise_for_status()

        except httpx.TimeoutException as e:
            raise AIRequestError(
                "LLM request timed out."
            ) from e

        except httpx.HTTPError as e:
            raise AIRequestError(
                f"LLM request failed: {e}"
            ) from e

        try:
            data = response.json()

            return data["choices"][0]["message"]["content"]

        except (
            ValueError,
            KeyError,
            IndexError,
            TypeError
        ) as e:
            raise AIRequestError(
                "LLM returned an unexpected response format."
            ) from e


llm_client = LLMClient()