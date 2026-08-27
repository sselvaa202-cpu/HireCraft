# HireCraft - AI Token Usage Tracking


from dataclasses import dataclass


@dataclass
class TokenUsage:
    """
    Represents token usage returned by an LLM request.
    """

    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0

    @classmethod
    def from_response(cls, usage: dict | None) -> "TokenUsage":
        """
        Create TokenUsage from an LLM response usage object.
        """

        if not usage:
            return cls()

        prompt_tokens = int(
            usage.get("prompt_tokens", 0)
        )

        completion_tokens = int(
            usage.get("completion_tokens", 0)
        )

        total_tokens = int(
            usage.get(
                "total_tokens",
                prompt_tokens + completion_tokens
            )
        )

        return cls(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
        )