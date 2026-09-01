# HireCraft - LinkedIn Strategy Service

from app.schemas.linkedin import LinkedInPlan


# Temporary deterministic skill mapping.
#
# This does NOT connect to an LLM.
# Later, this can be replaced/enhanced by AIService.

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


def extract_skills_from_job_description(
    job_description: str,
) -> list[str]:
    """
    Extract known technical skills from the job description.

    Only skills explicitly present in the JD are returned.
    """

    text = job_description.lower()

    known_skills = [
        "python",
        "fastapi",
        "django",
        "flask",
        "java",
        "javascript",
        "typescript",
        "react",
        "html",
        "css",
        "sql",
        "mysql",
        "postgresql",
        "mongodb",
        "git",
        "github",
        "docker",
        "aws",
        "azure",
        "rest api",
        "api",
        "machine learning",
        "deep learning",
        "pandas",
        "numpy",
        "excel",
        "power bi",
    ]

    found_skills = []

    for skill in known_skills:

        if skill in text:
            found_skills.append(skill.title())

    return found_skills


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


def generate_linkedin_plan(
    target_role: str | None = None,
    job_description: str | None = None,
) -> LinkedInPlan:
    """
    Generate a LinkedIn strategy using ONLY:

    - target_role
    OR
    - job_description

    No previous LinkedIn profile data is used.
    """

    # 1. Determine target role

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


    # 2. Determine required skills

    if job_description:

        skills = extract_skills_from_job_description(
            job_description
        )

    else:

        skills = get_role_skills(
            target_role
        )


    # 3. Profile strategy

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


    # 5. About section

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


    # 6. Skills to highlight

    skills_to_highlight = skills


    # 7. Content strategy

    content_strategy = [
        f"Create posts related to {target_role}.",
        "Share practical learning and project-building experiences.",
        "Explain technical concepts related to the target role.",
        "Share completed projects with clear technical explanations.",
    ]


    # 8. Posting plan

    posting_plan = [
        "Post 2-3 times per week.",
        "Share one technical learning post each week.",
        "Share project progress or project demonstrations.",
        "Share practical lessons learned from development work.",
    ]


    # 9. Networking strategy

    networking_strategy = [
        f"Connect with professionals working as {target_role}.",
        "Follow companies hiring for the target role.",
        "Engage with relevant technical posts.",
        "Write meaningful comments on industry discussions.",
        "Build connections with recruiters and hiring managers.",
    ]


    # 10. Job search strategy

    job_search_strategy = [
        f"Search for {target_role} opportunities.",
        "Use the extracted job skills as LinkedIn search keywords.",
        "Follow companies that regularly hire for the target role.",
        "Review job descriptions and identify recurring technical requirements.",
        "Apply to relevant entry-level and junior opportunities.",
    ]


    # 11. Return structured LinkedIn plan

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
    )