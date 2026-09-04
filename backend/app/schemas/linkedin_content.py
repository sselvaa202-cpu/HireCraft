# HireCraft - LinkedIn Content Intelligence Schemas

from pydantic import BaseModel, Field


class LinkedInContentPlan(BaseModel):
    """
    Structured LinkedIn content strategy generated
    only from the target role and required skills.

    No existing LinkedIn profile data is used.
    """

    content_pillars: list[str] = Field(
        default_factory=list
    )

    post_topics: list[str] = Field(
        default_factory=list
    )

    technical_post_ideas: list[str] = Field(
        default_factory=list
    )

    project_post_ideas: list[str] = Field(
        default_factory=list
    )

    learning_post_ideas: list[str] = Field(
        default_factory=list
    )

    engagement_topics: list[str] = Field(
        default_factory=list
    )

    thirty_day_content_direction: list[str] = Field(
        default_factory=list
    )