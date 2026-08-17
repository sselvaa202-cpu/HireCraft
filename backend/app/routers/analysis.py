from fastapi import APIRouter
from app.schemas.career import CareerProfile

router = APIRouter(
    prefix="/api",
    tags=["Analysis"]
)


@router.post("/analyze")
def analyze_profile(profile: CareerProfile):
    return {
        "message": "Career profile received successfully",
        "profile": profile
    }