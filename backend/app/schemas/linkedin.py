from pydantic import BaseModel, Field


class LinkedInRequest(BaseModel):
    """
    Input required to generate a LinkedIn plan.

    HireCraft uses only the target role and job requirements.
    """

    target_role: str = Field(
        ...,
        min_length=2
    )

    required_skills: list[str] = Field(
        default_factory=list
    )


class LinkedInPlan(BaseModel):
    """
    Structured LinkedIn strategy generated from
    a target job description or target role.
    """

    target_role: str = Field(default="Not specified")

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