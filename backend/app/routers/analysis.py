from fastapi import APIRouter, HTTPException

from app.schemas.career import CareerProfile
from app.services.analysis import analyze_career_profile
from app.services.job_analysis import analyze_job_description


router = APIRouter(
    prefix="/api",
    tags=["Analysis"]
)


@router.post("/analyze")
def analyze_profile(profile: CareerProfile):

    try:

        # Analyze the target job description
        job_requirements = analyze_job_description(
            profile.target_job_description
        )

        # Analyze the career profile
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