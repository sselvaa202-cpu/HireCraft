# HireCraft - LinkedIn Profile Optimization Schemas

from pydantic import BaseModel, Field


class LinkedInProfileOptimization(BaseModel):
    """
    LinkedIn profile optimization strategy generated
    from a target role and required skills.

    No existing LinkedIn profile is required.
    """

    headline_variants: list[str] = Field(
        default_factory=list
    )

    about_structure: list[str] = Field(
        default_factory=list
    )

    keyword_strategy: list[str] = Field(
        default_factory=list
    )

    priority_skills: list[str] = Field(
        default_factory=list
    )

    featured_section_strategy: list[str] = Field(
        default_factory=list
    )

    project_visibility_strategy: list[str] = Field(
        default_factory=list
    )

    profile_keyword_map: dict[str, list[str]] = Field(
        default_factory=dict
    )