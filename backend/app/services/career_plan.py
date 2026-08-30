# HireCraft - Career Plan Service

from app.services.job_analysis import analyze_job_description
from app.services.linkedin import generate_linkedin_plan


def generate_career_plan(job_description: str):
    """
    Generate a complete career plan from a job description.

    Current flow:
        Job Description
            ↓
        Job Analysis
            ↓
        LinkedIn Plan
    """

    # Step 1: Analyze the job description
    job_requirements = analyze_job_description(
        job_description
    )

    # Step 2: Generate LinkedIn plan
    linkedin_plan = generate_linkedin_plan(
        target_role=job_requirements.job_title,
        required_skills=job_requirements.required_skills,
    )

    return {
        "job_requirements": job_requirements,
        "linkedin_plan": linkedin_plan,
    }