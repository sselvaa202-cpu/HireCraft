from fastapi import APIRouter, HTTPException

from app.schemas.career import CareerProfile
from app.services.analysis import analyze_career_profile
from app.ai.service import analyze_job_with_ai


router = APIRouter(
    prefix="/api",
    tags=["Analysis"]
)


@router.post("/analyze")
def analyze_profile(profile: CareerProfile):

    try:

        # AI analysis with Phase 4 fallback
        job_requirements = analyze_job_with_ai(
            profile.target_job_description
        )

        # Compare career profile with job requirements
        analysis = analyze_career_profile(
            profile,
            job_requirements
        )

        return {
            "status": "success",
            "message": "Career analysis completed successfully",
            "data": {
                "profile": profile,
                "job_requirements": job_requirements,
                "analysis": analysis
            }
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Career analysis failed: {str(e)}"
        )