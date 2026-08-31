# HireCraft - LinkedIn Router

from fastapi import APIRouter

from app.schemas.linkedin import (
    LinkedInRequest,
    LinkedInPlan,
)

from app.services.career_plan import generate_career_plan


router = APIRouter(
    prefix="/api/linkedin",
    tags=["LinkedIn"],
)


@router.post(
    "/plan",
    response_model=LinkedInPlan,
)
def create_linkedin_plan(
    request: LinkedInRequest,
) -> LinkedInPlan:

    result = generate_career_plan(
        job_description=request.job_description
    )

    return result["linkedin_plan"]