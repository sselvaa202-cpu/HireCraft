# HireCraft - GitHub Alignment & Recommendation Service

from typing import Any


# Role-specific GitHub recommendations

ROLE_RECOMMENDATIONS = {
    "backend developer": {
        "important_skills": [
            "Python",
            "FastAPI",
            "PostgreSQL",
            "Git",
            "REST API",
            "SQL",
        ],
        "recommended_project_types": [
            "REST API backend",
            "FastAPI + PostgreSQL application",
            "Authentication and authorization system",
            "Backend service with database integration",
        ],
    },

    "python developer": {
        "important_skills": [
            "Python",
            "SQL",
            "FastAPI",
            "Django",
            "Git",
        ],
        "recommended_project_types": [
            "Python backend application",
            "REST API",
            "Automation project",
            "Database-driven Python application",
        ],
    },

    "frontend developer": {
        "important_skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git",
        ],
        "recommended_project_types": [
            "React application",
            "Responsive frontend",
            "Dashboard",
            "API-integrated frontend",
        ],
    },

    "full stack developer": {
        "important_skills": [
            "Python",
            "JavaScript",
            "React",
            "SQL",
            "PostgreSQL",
            "Git",
        ],
        "recommended_project_types": [
            "Full-stack web application",
            "React + FastAPI application",
            "Authentication system",
            "Database-driven application",
        ],
    },

    "software engineer": {
        "important_skills": [
            "Python",
            "SQL",
            "Git",
            "REST API",
            "Docker",
        ],
        "recommended_project_types": [
            "Production-style backend application",
            "API service",
            "Software architecture project",
            "Dockerized application",
        ],
    },
}


# Helpers

def normalize_skill(skill: str) -> str:
    """
    Normalize skill names for comparison.
    """

    aliases = {
        "fastapi": "fastapi",
        "fast api": "fastapi",
        "postgres": "postgresql",
        "postgresql": "postgresql",
        "python": "python",
        "git": "git",
        "github": "git",
        "rest api": "rest api",
        "api": "api",
        "sql": "sql",
        "mysql": "mysql",
        "javascript": "javascript",
        "react": "react",
        "django": "django",
        "docker": "docker",
    }

    value = skill.strip().lower()

    return aliases.get(value, value)


def unique_list(items: list[str]) -> list[str]:
    """
    Return a list without duplicates while preserving order.
    """

    result = []
    seen = set()

    for item in items:

        normalized = item.strip().lower()

        if normalized and normalized not in seen:
            seen.add(normalized)
            result.append(item)

    return result


def get_target_skills(
    target_role: str | None,
    job_description: str | None = None,
) -> list[str]:

    """
    Determine important skills from either:

    1. Target role
    2. Job description

    This is currently deterministic.

    Later the LLM can replace/enhance this logic.
    """

    skills = []

    # Role-based skills

    if target_role:

        role_key = target_role.strip().lower()

        role_data = ROLE_RECOMMENDATIONS.get(
            role_key,
            {}
        )

        skills.extend(
            role_data.get(
                "important_skills",
                []
            )
        )

    # JD-based skills

    if job_description:

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
            "docker",
            "aws",
            "azure",
            "rest api",
            "api",
            "pandas",
            "numpy",
        ]

        for skill in known_skills:

            if skill in text:

                formatted = skill.title()

                if skill == "fastapi":
                    formatted = "FastAPI"

                elif skill == "postgresql":
                    formatted = "PostgreSQL"

                elif skill == "rest api":
                    formatted = "REST API"

                elif skill == "api":
                    formatted = "API"

                skills.append(formatted)

    return unique_list(skills)


# Extract GitHub skills

def extract_github_skills(github_data):
    """
    Extract skills from GitHub profile and repository language data.
    """

    skills = set()

    # Profile-level skills from bio
    profile = github_data.get("profile", {})
    bio = profile.get("bio") or ""

    bio_lower = bio.lower()

    skill_keywords = {
        "python": "Python",
        "fastapi": "FastAPI",
        "postgresql": "PostgreSQL",
        "redis": "Redis",
        "rest api": "REST API",
        "sql": "SQL",
        "rag": "RAG",
        "llm": "LLM",
        "multi-agent": "Multi-Agent Systems",
        "ai orchestration": "AI Orchestration",
        "vector database": "Vector Databases",
        "vector databases": "Vector Databases",
    }

    for keyword, skill_name in skill_keywords.items():
        if keyword in bio_lower:
            skills.add(skill_name)

    # Repository languages
    repositories = github_data.get("repositories", [])

    for repository in repositories:
        languages = repository.get("languages", [])

        for language in languages:
            normalized = normalize_skill(language)

            if normalized:
                skills.add(normalized)

    return sorted(skills)


# Extract repository list

def extract_repositories(
    github_data: dict[str, Any],
) -> list[dict[str, Any]]:

    repositories = github_data.get(
        "repositories",
        []
    )

    if not isinstance(repositories, list):
        return []

    return repositories


# Find repository recommendations

def analyze_repository(
    repository: dict[str, Any],
    target_skills: list[str],
) -> dict[str, Any]:

    name = repository.get(
        "name",
        "Unknown Repository"
    )

    description = repository.get(
        "description"
    )

    languages = repository.get(
        "languages",
        []
    )

    topics = repository.get(
        "topics",
        []
    )

    # The collector currently provides repository languages directly.
    # Older alignment data may also contain matched_skills, so support both.
    matched_skills = repository.get(
        "matched_skills",
        []
    )

    technology_evidence = repository.get(
        "technology_evidence",
        []
    )

    if not isinstance(matched_skills, list):
        matched_skills = []

    if not isinstance(technology_evidence, list):
        technology_evidence = []

    recommendations = []

    # README

    has_readme = repository.get(
        "has_readme",
        True
    )

    if not has_readme:

        recommendations.append(
            "Add a clear README explaining the project purpose, setup, architecture, technologies and usage."
        )

    # Description

    if not description:

        recommendations.append(
            "Add a concise repository description explaining the project's purpose."
        )

    # Topics

    if not topics:

        recommendations.append(
            "Add relevant GitHub topics based on the project's technologies and purpose."
        )

    # Technology visibility

    repo_skills = [
        normalize_skill(skill)
        for skill in matched_skills
        if isinstance(skill, str)
    ]

    repo_languages = [
        normalize_skill(language)
        for language in languages
        if isinstance(language, str)
    ]

    visible_technologies = unique_list(
        [
            str(skill)
            for skill in matched_skills + languages
            if isinstance(skill, str)
        ]
    )

    # Target-role technology recommendations

    missing_from_repo = []

    for skill in target_skills:

        normalized_target = normalize_skill(
            skill
        )

        if (
            normalized_target not in repo_skills
            and normalized_target not in repo_languages
        ):

            missing_from_repo.append(
                skill
            )

    if missing_from_repo:

        recommendations.append(
            "If these technologies are genuinely used in the project, document them clearly in the README: "
            + ", ".join(missing_from_repo)
            + "."
        )

    # Architecture

    repository_files = repository.get(
        "files",
        repository.get("structure", [])
    )

    if isinstance(repository_files, list):

        has_backend_structure = any(
            str(item).lower() in {
                "backend",
                "app",
                "api",
                "server",
                "src",
            }
            for item in repository_files
        )

        if has_backend_structure:

            recommendations.append(
                "Document the backend architecture and explain the main modules and responsibilities."
            )

    # Final repository result

    return {
        "repository": name,
        "visible_technologies": visible_technologies,
        "matched_target_skills": [
            skill
            for skill in target_skills
            if normalize_skill(skill)
            in repo_skills + repo_languages
        ],
        "missing_target_skills": missing_from_repo,
        "recommendations": unique_list(
            recommendations
        ),
    }


# Profile recommendations

def generate_profile_recommendations(
    github_data: dict[str, Any],
    target_role: str,
    target_skills: list[str],
) -> list[str]:

    recommendations = []

    repositories = extract_repositories(
        github_data
    )

    github_skills = extract_github_skills(
        github_data
    )

    # Profile README

    profile_repo = None

    profile = github_data.get("profile", {})
    username = profile.get("username")

    for repo in repositories:

        repo_name = str(
            repo.get("name", "")
        ).lower()

        if username and repo_name == username.lower():

            profile_repo = repo
            break

    if profile_repo:

        recommendations.append(
            "Use the GitHub profile README to clearly position the profile toward "
            + target_role
            + "."
        )

    else:

        recommendations.append(
            "Create or improve the GitHub profile README with a clear career direction toward "
            + target_role
            + "."
        )

    # Skills

    missing_skills = []

    normalized_github = [
        normalize_skill(skill)
        for skill in github_skills
    ]

    for skill in target_skills:

        if normalize_skill(skill) not in normalized_github:

            missing_skills.append(
                skill
            )

    if missing_skills:

        recommendations.append(
            "Increase genuine GitHub evidence for these target-role skills through real projects and clear documentation: "
            + ", ".join(missing_skills)
            + "."
        )

    # Project visibility

    if repositories:

        recommendations.append(
            "Feature the strongest repositories that demonstrate the target role."
        )

        recommendations.append(
            "Keep repository names, descriptions, README files and topics consistent with the target career direction."
        )

    return unique_list(
        recommendations
    )


# New project recommendations

def generate_project_recommendations(
    target_role: str,
    target_skills: list[str],
    github_data: dict[str, Any],
) -> list[str]:

    role_key = target_role.strip().lower()

    role_data = ROLE_RECOMMENDATIONS.get(
        role_key,
        {}
    )

    recommended_projects = role_data.get(
        "recommended_project_types",
        []
    )

    github_skills = extract_github_skills(
        github_data
    )

    normalized_github = [
        normalize_skill(skill)
        for skill in github_skills
    ]

    recommendations = []

    # Prefer projects that address skills not currently visible in
    # the GitHub evidence. If there are no gaps, still recommend
    # projects that strengthen the target-role portfolio.

    missing_skills = [
        skill
        for skill in target_skills
        if normalize_skill(skill) not in normalized_github
    ]

    skills_to_demonstrate = (
        missing_skills[:4]
        if missing_skills
        else target_skills[:4]
    )

    for project in recommended_projects:

        if skills_to_demonstrate:

            recommendations.append(
                f"Consider building a {project} that genuinely demonstrates "
                + ", ".join(skills_to_demonstrate)
                + "."
            )

    # Fallback

    if not recommendations:

        recommendations.append(
            "Build one focused project that demonstrates the core technologies required for the target role."
        )

    return unique_list(
        recommendations
    )


# Main alignment function

def generate_github_recommendation_plan(
    github_data: dict[str, Any],
    target_role: str | None = None,
    job_description: str | None = None,
) -> dict[str, Any]:

    """
    Generate a GitHub improvement plan.

    Important:
    This function does NOT produce a score.

    It produces actionable recommendations.
    """

    if not target_role:

        target_role = "Software Engineer"

    target_role = target_role.strip()

    # 1. Determine target skills

    target_skills = get_target_skills(
        target_role=target_role,
        job_description=job_description,
    )

    # 2. Extract GitHub skills

    github_skills = extract_github_skills(
        github_data
    )

    # 3. Repository analysis

    repositories = extract_repositories(
        github_data
    )

    repository_recommendations = []

    for repository in repositories:

        repository_result = analyze_repository(
            repository=repository,
            target_skills=target_skills,
        )

        repository_recommendations.append(
            repository_result
        )

    # 4. Profile recommendations

    profile_recommendations = (
        generate_profile_recommendations(
            github_data=github_data,
            target_role=target_role,
            target_skills=target_skills,
        )
    )

    # 5. Project recommendations

    project_recommendations = (
        generate_project_recommendations(
            target_role=target_role,
            target_skills=target_skills,
            github_data=github_data,
        )
    )

    # 6. Missing skills

    normalized_github_skills = [
        normalize_skill(skill)
        for skill in github_skills
    ]

    missing_skills = []

    for skill in target_skills:

        if normalize_skill(skill) not in normalized_github_skills:

            missing_skills.append(
                skill
            )

    # 7. Priority actions

    priority_actions = []

    priority_actions.extend(
        profile_recommendations[:3]
    )

    for repository in repository_recommendations:

        recommendations = repository.get(
            "recommendations",
            []
        )

        if recommendations:

            priority_actions.append(
                f"{repository['repository']}: "
                + recommendations[0]
            )

    if missing_skills:

        priority_actions.append(
            "Build genuine project evidence for: "
            + ", ".join(missing_skills)
            + "."
        )

    # 8. Final response

    return {
        "target_role": target_role,

        "github_username": github_data.get(
            "profile", {}
        ).get("username"),

        "target_skills": target_skills,

        "github_skills": github_skills,

        "missing_skills": missing_skills,

        "profile_recommendations":
            profile_recommendations,

        "repository_recommendations":
            repository_recommendations,

        "new_project_recommendations":
            project_recommendations,

        "priority_actions":
            unique_list(priority_actions),
    }