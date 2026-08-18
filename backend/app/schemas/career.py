from pydantic import BaseModel, Field


class CareerProfile(BaseModel):
    full_name: str = Field(..., min_length=3)
    current_role: str
    skills: str
    experience: str
    projects: str
    education: str
    target_job_description: str