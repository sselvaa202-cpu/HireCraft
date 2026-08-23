from pydantic_settings import BaseSettings, SettingsConfigDict


class AISettings(BaseSettings):
    """
    Configuration for HireCraft AI infrastructure.
    """

    llm_api_key: str = ""
    llm_provider: str = ""
    llm_model: str = ""
    llm_base_url: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


ai_settings = AISettings()