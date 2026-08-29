# HireCraft - LinkedIn Strategy Service

from app.schemas.linkedin import LinkedInPlan


def generate_linkedin_plan(
    target_role: str,
    required_skills: list[str],
) -> LinkedInPlan:
    """
    Generate a LinkedIn strategy based only on
    the target role and required job skills.

    No previous profile data is used.
    """

    target_role = target_role.strip()

    skills = [
        skill.strip()
        for skill in required_skills
        if skill.strip()
    ]

    # Profile strategy
    profile_strategy = [
        f"Position your LinkedIn profile toward {target_role} roles.",
        "Keep your profile focused on the target career direction.",
        "Highlight projects and technical skills relevant to the target role.",
    ]

    # Headline
    if skills:
        headline = (
            f"{target_role} | "
            + " | ".join(skill.title() for skill in skills[:4])
            + " | Open to Opportunities"
        )
    else:
        headline = f"{target_role} | Open to Opportunities"

    # About section
    if skills:
        skills_text = ", ".join(skill.title() for skill in skills)

        about_section = (
            f"Aspiring {target_role} focused on building practical "
            f"software solutions and continuously improving technical skills "
            f"including {skills_text}. "
            f"Interested in opportunities where I can apply these skills, "
            f"work on real-world projects, and grow as a professional."
        )
    else:
        about_section = (
            f"Aspiring {target_role} focused on building practical "
            "projects, developing technical skills, and growing through "
            "real-world software development opportunities."
        )

    # Skills
    skills_to_highlight = [
        skill.title()
        for skill in skills
    ]

    # Content strategy
    content_strategy = [
        f"Create posts related to {target_role}.",
        "Share practical learning and project-building experiences.",
        "Explain technical concepts related to the target role.",
        "Share completed projects with clear technical explanations.",
    ]

    # Posting plan
    posting_plan = [
        "Post 2-3 times per week.",
        "Share one technical learning post each week.",
        "Share project progress or project demonstrations.",
        "Share practical lessons learned from development work.",
    ]

    # Networking
    networking_strategy = [
        f"Connect with professionals working as {target_role}.",
        "Follow companies hiring for the target role.",
        "Engage with relevant technical posts.",
        "Write meaningful comments on industry discussions.",
        "Build connections with recruiters and hiring managers.",
    ]

    # Job search
    job_search_strategy = [
        f"Search for {target_role} opportunities.",
        "Use the extracted job skills as LinkedIn search keywords.",
        "Follow companies that regularly hire for the target role.",
        "Review job descriptions and identify recurring technical requirements.",
        "Apply to relevant entry-level and junior opportunities.",
    ]

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