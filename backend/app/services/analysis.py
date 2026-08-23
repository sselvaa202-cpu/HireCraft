from app.schemas.career import CareerProfile
from app.schemas.analysis import AnalysisResult, SkillGap
from app.schemas.job import JobRequirement


def analyze_career_profile(
    profile: CareerProfile,
    job: JobRequirement
) -> AnalysisResult:
    """
    Analyze a career profile against structured job requirements.
    """

    # Required skills from the analyzed job description
    required_skills = {
        skill.strip().lower()
        for skill in job.required_skills
        if skill.strip()
    }

    # User skills
    user_skills = {
        skill.strip().lower()
        for skill in profile.skills.split(",")
        if skill.strip()
    }

    # Matched skills
    matched_skills = sorted(
        user_skills.intersection(required_skills)
    )

    # Missing skills
    missing_skills = sorted(
        required_skills.difference(user_skills)
    )

    # Skill gaps
    skill_gaps = []

    for skill in missing_skills:

        if skill in {
            "python",
            "sql",
            "fastapi",
            "postgresql"
        }:
            priority = "high"

        elif skill in {
            "javascript",
            "react",
            "git",
            "docker"
        }:
            priority = "medium"

        else:
            priority = "low"

        skill_gaps.append(
            SkillGap(
                skill=skill,
                priority=priority
            )
        )

    # Match percentage
    if required_skills:
        match_percentage = (
            len(matched_skills)
            / len(required_skills)
        ) * 100
    else:
        match_percentage = 0.0

    # Strengths
    strengths = matched_skills.copy()

    # Priority ordering
    priority_order = {
        "high": 1,
        "medium": 2,
        "low": 3
    }

    skill_gaps.sort(
        key=lambda gap: priority_order[gap.priority]
    )

    # Skill display names
    skill_display_names = {
        "python": "Python",
        "sql": "SQL",
        "fastapi": "FastAPI",
        "postgresql": "PostgreSQL",
        "git": "Git",
        "html": "HTML",
        "css": "CSS",
        "javascript": "JavaScript",
        "react": "React",
        "excel": "Excel",
        "power bi": "Power BI",
        "statistics": "Statistics",
        "docker": "Docker",
        "data structures": "Data Structures",
        "algorithms": "Algorithms"
    }

    # Recommendations
    recommendations = []

    for gap in skill_gaps:

        skill_name = skill_display_names.get(
            gap.skill,
            gap.skill.title()
        )

        recommendations.append(
            f"Learn {skill_name} — "
            f"{gap.priority.title()} Priority"
        )

    return AnalysisResult(
        match_percentage=round(match_percentage, 2),
        matched_skills=matched_skills,
        skill_gaps=skill_gaps,
        strengths=strengths,
        recommendations=recommendations
    )