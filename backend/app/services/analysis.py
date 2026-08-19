from app.schemas.career import CareerProfile
from app.schemas.analysis import AnalysisResult


JOB_SKILLS = {
    "python developer": {
        "python",
        "sql",
        "git",
        "fastapi",
        "postgresql"
    },

    "backend developer": {
        "python",
        "sql",
        "fastapi",
        "postgresql",
        "git"
    },

    "frontend developer": {
        "html",
        "css",
        "javascript",
        "react",
        "git"
    },

    "full stack developer": {
        "html",
        "css",
        "javascript",
        "react",
        "python",
        "sql",
        "git"
    },

    "data analyst": {
        "python",
        "sql",
        "excel",
        "power bi",
        "statistics"
    },

    "software engineer": {
        "python",
        "sql",
        "git",
        "data structures",
        "algorithms"
    }
}


def get_required_skills(target_job: str) -> set[str]:
    """
    Return required skills for the requested job.
    """

    job = target_job.strip().lower()

    return JOB_SKILLS.get(
        job,
        {
            "python",
            "sql",
            "git"
        }
    )


def analyze_career_profile(profile: CareerProfile) -> AnalysisResult:
    """
    Analyze a career profile against job-specific skills.
    """

    required_skills = get_required_skills(
        profile.target_job_description
    )

    user_skills = {
        skill.strip().lower()
        for skill in profile.skills.split(",")
        if skill.strip()
    }

    matched_skills = sorted(
        user_skills.intersection(required_skills)
    )

    skill_gaps = sorted(
        required_skills.difference(user_skills)
    )

    if required_skills:
        match_percentage = (
            len(matched_skills) / len(required_skills)
        ) * 100
    else:
        match_percentage = 0.0

    strengths = matched_skills.copy()

    recommendations = [
        f"Learn {skill.title()}"
        for skill in skill_gaps
    ]

    return AnalysisResult(
        match_percentage=round(match_percentage, 2),
        matched_skills=matched_skills,
        skill_gaps=skill_gaps,
        strengths=strengths,
        recommendations=recommendations
    )