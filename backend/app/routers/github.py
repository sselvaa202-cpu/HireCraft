# HireCraft - GitHub Router

from fastapi import APIRouter

from app.schemas.github import (
    GitHubRequest,
    GitHubPlan,
)

from app.services.github import generate_github_plan


router = APIRouter(
    prefix="/api/github",
    tags=["GitHub"],
)


@router.post(
    "/plan",
    response_model=GitHubPlan,
)
def create_github_plan(
    request: GitHubRequest,
) -> GitHubPlan:

    return generate_github_plan(
        target_role=request.target_role,
        job_description=request.job_description,
    )