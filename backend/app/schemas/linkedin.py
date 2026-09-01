# HireCraft - LinkedIn Schemas

from pydantic import BaseModel, Field, model_validator


class LinkedInRequest(BaseModel):
    """
    User provides either:
    1. target_role
    OR
    2. job_description

    HireCraft generates the LinkedIn plan internally.

    No existing LinkedIn profile information is required.
    """

    target_role: str | None = Field(
        default=None,
        min_length=2
    )

    job_description: str | None = Field(
        default=None,
        min_length=20
    )

    @model_validator(mode="after")
    def validate_input(self):
        """
        At least one of target_role or job_description
        must be provided.
        """

        if not self.target_role and not self.job_description:
            raise ValueError(
                "Provide either target_role or job_description."
            )

        return self


class LinkedInPlan(BaseModel):
    """
    Structured LinkedIn strategy generated from
    a target role or job description.
    """

    target_role: str = Field(
        default="Not specified"
    )

    profile_strategy: list[str] = Field(
        default_factory=list
    )

    headline: str = Field(
        default="Not specified"
    )

    about_section: str = Field(
        default="Not specified"
    )

    skills_to_highlight: list[str] = Field(
        default_factory=list
    )

    content_strategy: list[str] = Field(
        default_factory=list
    )

    posting_plan: list[str] = Field(
        default_factory=list
    )

    networking_strategy: list[str] = Field(
        default_factory=list
    )

    job_search_strategy: list[str] = Field(
        default_factory=list
    )