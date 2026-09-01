# HireCraft - LinkedIn Search Intelligence Service

from app.schemas.linkedin_search import LinkedInSearchPlan


def generate_linkedin_search_plan(
    target_role: str,
    required_skills: list[str],
) -> LinkedInSearchPlan:
    """
    Generate LinkedIn search intelligence using only:

    - Target role
    - Required job skills

    No existing LinkedIn profile data is used.
    """

    target_role = target_role.strip()

    # Clean skills
    skills = [
        skill.strip()
        for skill in required_skills
        if skill and skill.strip()
    ]

    # Remove duplicates while preserving order
    skills = list(dict.fromkeys(skills))

    # Primary titles

    primary_titles = [
        target_role,
    ]

    # Add a developer/engineer variation when useful
    role_lower = target_role.lower()

    if "developer" in role_lower:
        primary_titles.append(
            target_role.replace("Developer", "Developer").strip()
        )

    elif "engineer" in role_lower:
        primary_titles.append(
            target_role
        )

    # Remove duplicates
    primary_titles = list(dict.fromkeys(primary_titles))

    # Related titles

    related_titles = []

    if "backend" in role_lower:
        related_titles = [
            "Backend Developer",
            "Python Developer",
            "Python Backend Developer",
            "Junior Backend Developer",
            "Software Engineer",
        ]

    elif "frontend" in role_lower:
        related_titles = [
            "Frontend Developer",
            "Web Developer",
            "React Developer",
            "Junior Frontend Developer",
            "UI Developer",
        ]

    elif "full stack" in role_lower or "fullstack" in role_lower:
        related_titles = [
            "Full Stack Developer",
            "Fullstack Developer",
            "Software Engineer",
            "Web Developer",
            "Junior Full Stack Developer",
        ]

    elif "data analyst" in role_lower:
        related_titles = [
            "Data Analyst",
            "Junior Data Analyst",
            "Business Data Analyst",
            "Reporting Analyst",
            "Data Analytics Associate",
        ]

    elif "software engineer" in role_lower:
        related_titles = [
            "Software Engineer",
            "Junior Software Engineer",
            "Software Developer",
            "Backend Developer",
            "Application Developer",
        ]

    else:
        related_titles = [
            target_role,
            f"Junior {target_role}",
        ]

    # Remove target role duplication
    related_titles = [
        title
        for title in related_titles
        if title.lower() != target_role.lower()
    ]

    # Skill keywords

    skill_keywords = [
        skill.title()
        for skill in skills
    ]

    # Search combinations

    search_combinations = []

    if target_role:
        search_combinations.append(target_role)

    # Role + individual skills
    for skill in skills[:5]:
        search_combinations.append(
            f"{target_role} {skill}"
        )

    # Skill-to-skill combinations
    for i in range(min(len(skills), 4)):
        for j in range(i + 1, min(len(skills), 4)):
            search_combinations.append(
                f"{skills[i]} {skills[j]}"
            )

    # Remove duplicates
    search_combinations = list(
        dict.fromkeys(search_combinations)
    )

    # Boolean searches

    boolean_searches = []

    if target_role and skills:

        # Main role + skills
        role_part = (
            f'"{target_role}"'
        )

        skill_part = " OR ".join(
            skill.title()
            for skill in skills[:3]
        )

        boolean_searches.append(
            f'{role_part} AND ({skill_part})'
        )

        # Role variations
        title_part = " OR ".join(
            f'"{title}"'
            for title in [target_role] + related_titles[:3]
        )

        boolean_searches.append(
            f'({title_part}) AND ({skill_part})'
        )

    elif target_role:

        boolean_searches.append(
            f'"{target_role}"'
        )

    # Return structured result

    return LinkedInSearchPlan(
        primary_titles=primary_titles,
        related_titles=related_titles,
        skill_keywords=skill_keywords,
        search_combinations=search_combinations,
        boolean_searches=boolean_searches,
    )