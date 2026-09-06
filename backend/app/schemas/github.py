# HireCraft - GitHub Schemas

from pydantic import BaseModel, Field, model_validator


class GitHubRequest(BaseModel):
    """
    User provides only:
    1. target_role
    OR
    2. job_description

    HireCraft generates the GitHub strategy internally.

    No existing GitHub profile or repository information
    is required from the user.
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


class GitHubPlan(BaseModel):
    """
    Complete GitHub strategy generated from
    a target role or job description.
    """

    target_role: str = Field(
        default="Not specified"
    )

    repository_strategy: list[str] = Field(
        default_factory=list
    )

    project_recommendations: list[str] = Field(
        default_factory=list
    )

    technology_focus: list[str] = Field(
        default_factory=list
    )

    repository_naming_strategy: list[str] = Field(
        default_factory=list
    )

    readme_strategy: list[str] = Field(
        default_factory=list
    )

    github_activity_strategy: list[str] = Field(
        default_factory=list
    )

    contribution_strategy: list[str] = Field(
        default_factory=list
    )

    keyword_strategy: list[str] = Field(
        default_factory=list
    )