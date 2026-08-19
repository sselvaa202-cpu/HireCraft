from fastapi import APIRouter, HTTPException

from app.schemas.career import CareerProfile
from app.services.analysis import analyze_career_profile


router = APIRouter(
    prefix="/api",
    tags=["Analysis"]
)


@router.post("/analyze")
def analyze_profile(profile: CareerProfile):

    try:

        analysis = analyze_career_profile(profile)

        return {
            "status": "success",
            "message": "Career analysis completed successfully",
            "data": {
                "profile": profile,
                "analysis": analysis
            }
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Career analysis failed: {str(e)}"
        )