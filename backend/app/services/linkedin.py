# HireCraft - LinkedIn Strategy Service

from app.schemas.linkedin import LinkedInPlan
from app.services.linkedin_search import generate_linkedin_search_plan
import re


# Temporary deterministic skill mapping
#
# This does NOT connect to an LLM.
# Later, this can be replaced/enhanced by AIService.
#
# These skills are used only when the user provides
# a target role without a job description.

ROLE_SKILLS = {
    "backend developer": [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "Git",
    ],

    "python developer": [
        "Python",
        "SQL",
        "FastAPI",
        "Git",
    ],

    "frontend developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Git",
    ],

    "full stack developer": [
        "Python",
        "JavaScript",
        "React",
        "SQL",
        "PostgreSQL",
        "Git",
    ],

    "software engineer": [
        "Python",
        "SQL",
        "Git",
        "Docker",
        "REST API",
    ],

    "data analyst": [
        "Python",
        "SQL",
        "Pandas",
        "Excel",
        "Power BI",
    ],
}

# Canonical Skill Names

SKILL_DISPLAY_NAMES = {
    "python": "Python",
    "fastapi": "FastAPI",
    "django": "Django",
    "flask": "Flask",
    "java": "Java",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "react": "React",
    "html": "HTML",
    "css": "CSS",
    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "mongodb": "MongoDB",
    "git": "Git",
    "github": "GitHub",
    "docker": "Docker",
    "aws": "AWS",
    "azure": "Azure",
    "rest api": "REST API",
    "api": "API",
    "machine learning": "Machine Learning",
    "deep learning": "Deep Learning",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "excel": "Excel",
    "power bi": "Power BI",
}


# Skill extraction from Job Description

def extract_skills_from_job_description(
    job_description: str,
) -> list[str]:
    """
    Extract known technical skills from the job description.

    Only skills explicitly present in the JD are returned.
    """

    text = job_description.lower()

    known_skills = list(SKILL_DISPLAY_NAMES.keys())

    found_skills = []

    # Check longer phrases first
    known_skills.sort(
        key=len,
        reverse=True
    )

    for skill in known_skills:

        pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text):

            found_skills.append(
                SKILL_DISPLAY_NAMES[skill]
            )

    return found_skills


# Get skills from target role

def get_role_skills(
    target_role: str,
) -> list[str]:
    """
    Get known skills for a target role.

    Used only when the user provides a target role
    without a job description.
    """

    role = target_role.strip().lower()

    return ROLE_SKILLS.get(role, [])


# Generate LinkedIn Plan

def generate_linkedin_plan(
    target_role: str | None = None,
    job_description: str | None = None,
) -> LinkedInPlan:
    """
    Generate a complete LinkedIn strategy using ONLY:

    - target_role
    OR
    - job_description

    No previous LinkedIn profile data is used.

    The generated plan contains:

    1. Profile strategy
    2. Headline
    3. About section
    4. Skills to highlight
    5. Content strategy
    6. Posting plan
    7. Networking strategy
    8. Job search strategy
    9. LinkedIn search intelligence
    """

    # 1. Determine Target Role

    if job_description:

        job_description = job_description.strip()

        extracted_role = None

        job_titles = [
            "backend developer",
            "frontend developer",
            "full stack developer",
            "software engineer",
            "python developer",
            "ai engineer",
            "machine learning engineer",
            "data engineer",
            "data analyst",
        ]

        text = job_description.lower()

        for title in job_titles:

            if title in text:
                extracted_role = title.title()
                break

        if extracted_role:

            target_role = extracted_role

        elif target_role:

            target_role = target_role.strip()

        else:

            target_role = "Not specified"

    elif target_role:

        target_role = target_role.strip()

    else:

        target_role = "Not specified"


    # 2. Determine Required Skills

    if job_description:

        skills = extract_skills_from_job_description(
            job_description
        )

    else:

        skills = get_role_skills(
            target_role
        )


    # Remove duplicates while preserving order

    skills = list(
        dict.fromkeys(
            skill.strip()
            for skill in skills
            if skill and skill.strip()
        )
    )


    # 3. Profile Strategy

    profile_strategy = [
        f"Position your LinkedIn profile toward {target_role} roles.",
        "Keep your profile focused on the target career direction.",
        "Highlight projects and technical skills relevant to the target role.",
    ]


    # 4. Headline

    if skills:

        headline = (
            f"{target_role} | "
            + " | ".join(
                skill
                for skill in skills[:4]
            )
            + " | Open to Opportunities"
        )

    else:

        headline = (
            f"{target_role} | "
            "Open to Opportunities"
        )


    # 5. About Section

    if skills:

        skills_text = ", ".join(skills)

        about_section = (
            f"Aspiring {target_role} focused on building "
            f"practical software solutions and continuously "
            f"improving technical skills including "
            f"{skills_text}. "
            f"Interested in opportunities where I can apply "
            f"these skills, work on real-world projects, "
            f"and grow as a professional."
        )

    else:

        about_section = (
            f"Aspiring {target_role} focused on building "
            "practical projects, developing technical skills, "
            "and growing through real-world opportunities."
        )


    # 6. Skills to Highlight

    skills_to_highlight = skills


    # 7. Content Strategy

    content_strategy = [
        f"Create posts related to {target_role}.",
        "Share practical learning and project-building experiences.",
        "Explain technical concepts related to the target role.",
        "Share completed projects with clear technical explanations.",
    ]


    # 8. Posting Plan

    posting_plan = [
        "Post 2-3 times per week.",
        "Share one technical learning post each week.",
        "Share project progress or project demonstrations.",
        "Share practical lessons learned from development work.",
    ]


    # 9. Networking Strategy

    networking_strategy = [
        f"Connect with professionals working as {target_role}.",
        "Follow companies hiring for the target role.",
        "Engage with relevant technical posts.",
        "Write meaningful comments on industry discussions.",
        "Build connections with recruiters and hiring managers.",
    ]


    # 10. Job Search Strategy

    job_search_strategy = [
        f"Search for {target_role} opportunities.",
        "Use the extracted job skills as LinkedIn search keywords.",
        "Follow companies that regularly hire for the target role.",
        "Review job descriptions and identify recurring technical requirements.",
        "Apply to relevant entry-level and junior opportunities.",
    ]


    # 11. LinkedIn Search Intelligence
    #
    # This connects the separate LinkedIn Search Intelligence
    # service to the main LinkedIn Plan.
    #
    # Input:
    #     target_role
    #     skills
    #
    # Output:
    #     primary titles
    #     related titles
    #     skill keywords
    #     search combinations
    #     boolean searches

    search_plan = generate_linkedin_search_plan(
        target_role=target_role,
        required_skills=skills,
    )


    # 12. Return Complete LinkedIn Plan

    return LinkedInPlan(
        target_role=target_role,

        profile_strategy=profile_strategy,

        headline=headline,

        about_section=about_section,

        skills_to_highlight=skills_to_highlight,

        content_strategy=content_strategy,

        posting_plan=posting_plan,

        networking_strategy=networking_strategy,

        job_search_strategy=job_search_strategy,

        search_intelligence=search_plan,
    )