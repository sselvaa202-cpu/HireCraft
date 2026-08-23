from pydantic import BaseModel, Field


class JobRequirement(BaseModel):
    job_title: str = Field(default="Unknown")
    required_skills: list[str] = Field(default_factory=list)
    responsibilities: list[str] = Field(default_factory=list)
    experience_level: str = Field(default="Not specified")
    education: str = Field(default="Not specified")