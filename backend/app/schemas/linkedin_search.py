# HireCraft - LinkedIn Search Intelligence Schema

from pydantic import BaseModel, Field


class LinkedInSearchPlan(BaseModel):
    """
    Search strategy generated from a target role
    and job requirements.
    """

    primary_titles: list[str] = Field(
        default_factory=list
    )

    related_titles: list[str] = Field(
        default_factory=list
    )

    skill_keywords: list[str] = Field(
        default_factory=list
    )

    search_combinations: list[str] = Field(
        default_factory=list
    )

    boolean_searches: list[str] = Field(
        default_factory=list
    )