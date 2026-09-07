# HireCraft - GitHub Analysis Schemas

from pydantic import BaseModel, Field, model_validator


class GitHubAnalysisRequest(BaseModel):
    """
    Input required for GitHub Intelligence.

    User provides:
    1. GitHub profile URL
    AND
    2. target_role OR job_description
    """

    github_url: str = Field(
        ...,
        min_length=10
    )

    target_role: str | None = Field(
        default=None,
        min_length=2
    )

    job_description: str | None = Field(
        default=None,
        min_length=20
    )

    @model_validator(mode="after")
    def validate_target(self):

        if not self.target_role and not self.job_description:
            raise ValueError(
                "Provide either target_role or job_description."
            )

        return self


class GitHubProfileSummary(BaseModel):
    """
    Summary of the user's current GitHub profile.
    """

    username: str = "Not specified"

    bio: str | None = None

    public_repositories: int = 0

    followers: int = 0

    following: int = 0


class GitHubRepositoryAnalysis(BaseModel):
    """
    Analysis of an individual GitHub repository.
    """

    name: str

    description: str | None = None

    languages: list[str] = Field(
        default_factory=list
    )

    topics: list[str] = Field(
        default_factory=list
    )

    has_readme: bool = False

    recommendation: str = ""


class GitHubRecommendationPlan(BaseModel):
    """
    Personalized GitHub improvement plan.

    This is recommendation-based and does NOT
    use a numerical GitHub score.
    """

    target_role: str = "Not specified"

    github_username: str = "Not specified"

    current_github_summary: list[str] = Field(
        default_factory=list
    )

    strengths: list[str] = Field(
        default_factory=list
    )

    missing_or_weak_areas: list[str] = Field(
        default_factory=list
    )

    profile_recommendations: list[str] = Field(
        default_factory=list
    )

    repository_recommendations: list[str] = Field(
        default_factory=list
    )

    project_recommendations: list[str] = Field(
        default_factory=list
    )

    readme_recommendations: list[str] = Field(
        default_factory=list
    )

    github_activity_recommendations: list[str] = Field(
        default_factory=list
    )

    priority_actions: list[str] = Field(
        default_factory=list
    )

    repository_analysis: list[GitHubRepositoryAnalysis] = Field(
        default_factory=list
    )


class GitHubAnalysisResult(BaseModel):
    """
    Complete Phase 7 GitHub Intelligence response.
    """

    target_role: str = "Not specified"

    github_profile: GitHubProfileSummary

    recommendation_plan: GitHubRecommendationPlan