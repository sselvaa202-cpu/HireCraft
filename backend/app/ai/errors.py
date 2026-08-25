# HireCraft - AI Errors


class AIError(Exception):
    """
    Base exception for HireCraft AI errors.
    """
    pass


class AIConfigurationError(AIError):
    """
    Raised when the LLM configuration is missing
    or invalid.
    """
    pass


class AIRequestError(AIError):
    """
    Raised when communication with the LLM fails.
    """
    pass


class AIResponseError(AIError):
    """
    Raised when the LLM returns an invalid response.
    """
    pass