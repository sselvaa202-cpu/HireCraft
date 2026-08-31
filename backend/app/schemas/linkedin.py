from pydantic import BaseModel, Field


class LinkedInRequest(BaseModel):
    """
    User provides only the job description.

    HireCraft extracts the target role and required
    skills automatically from the job description.
    """

    target_role: str | None = None
    job_description: str | None = None


class LinkedInPlan(BaseModel):
    """
    Structured LinkedIn strategy generated from
    a job description.
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