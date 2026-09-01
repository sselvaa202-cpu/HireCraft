# HireCraft - LinkedIn Router

from fastapi import APIRouter

from app.schemas.linkedin import (
    LinkedInRequest,
    LinkedInPlan,
)

from app.services.linkedin import generate_linkedin_plan


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

    return generate_linkedin_plan(
        target_role=request.target_role,
        job_description=request.job_description,
    )