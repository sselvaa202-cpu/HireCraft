from fastapi import APIRouter, HTTPException

from app.schemas.career import CareerProfile


router = APIRouter(
    prefix="/api",
    tags=["Analysis"]
)


@router.post("/analyze")
def analyze_profile(profile: CareerProfile):

    try:

        return {
            "status": "success",
            "message": "Career profile received successfully",
            "data": {
                "profile": profile
            }
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Career analysis failed: {str(e)}"
        )