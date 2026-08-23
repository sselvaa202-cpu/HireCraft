from pydantic import BaseModel, Field, field_validator


class CareerProfile(BaseModel):

    full_name: str = Field(..., min_length=3)

    current_role: str

    skills: str

    experience: str

    projects: str

    education: str

    target_job_description: str = Field(
        ...,
        min_length=20,
        description="Job description to analyze"
    )

    @field_validator("target_job_description")
    @classmethod
    def validate_job_description(cls, value: str) -> str:

        value = value.strip()

        if not value:
            raise ValueError(
                "Job description cannot be empty"
            )

        return value