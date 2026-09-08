# HireCraft - GitHub Target Alignment

from typing import Any


def normalize(value: str) -> str:
    return value.strip().lower()


def collect_github_skills(
    repositories: list[dict[str, Any]],
) -> list[str]:
    """
    Collect all technologies detected across
    GitHub repositories.
    """

    skills = set()

    for repository in repositories:

        for language in repository.get(
            "languages",
            []
        ):
            skills.add(
                normalize(language)
            )

        for topic in repository.get(
            "topics",
            []
        ):
            skills.add(
                normalize(topic)
            )

    return sorted(skills)


def find_matching_skills(
    required_skills: list[str],
    github_skills: list[str],
) -> list[str]:
    """
    Find target skills that are already
    represented in the GitHub profile.
    """

    github_skills_normalized = {
        normalize(skill)
        for skill in github_skills
    }

    matches = []

    for skill in required_skills:

        if normalize(skill) in github_skills_normalized:
            matches.append(skill)

    return matches


def find_missing_skills(
    required_skills: list[str],
    github_skills: list[str],
) -> list[str]:
    """
    Find target skills that are not clearly
    represented in GitHub repository data.
    """

    github_skills_normalized = {
        normalize(skill)
        for skill in github_skills
    }

    missing = []

    for skill in required_skills:

        if normalize(skill) not in github_skills_normalized:
            missing.append(skill)

    return missing


def analyze_repository_alignment(
    repository: dict[str, Any],
    required_skills: list[str],
) -> dict[str, Any]:
    """
    Analyze one repository against target skills.
    """

    repository_skills = set()

    for language in repository.get(
        "languages",
        []
    ):
        repository_skills.add(
            normalize(language)
        )

    for topic in repository.get(
        "topics",
        []
    ):
        repository_skills.add(
            normalize(topic)
        )

    matched = []

    for skill in required_skills:

        if normalize(skill) in repository_skills:
            matched.append(skill)

    return {
        "name": repository.get(
            "name",
            "Unknown"
        ),

        "description": repository.get(
            "description"
        ),

        "matched_skills": matched,

        "languages": repository.get(
            "languages",
            []
        ),

        "topics": repository.get(
            "topics",
            []
        ),

        "has_readme": repository.get(
            "has_readme",
            False
        ),
    }


def generate_github_alignment(
    github_data: dict[str, Any],
    target_role: str,
    required_skills: list[str],
) -> dict[str, Any]:
    """
    Compare the current GitHub profile with
    the requirements of the target role.

    No numerical scoring is used.
    """

    profile = github_data.get(
        "profile",
        {}
    )

    repositories = github_data.get(
        "repositories",
        []
    )

    # 1. Collect GitHub technologies

    github_skills = collect_github_skills(
        repositories
    )

    # 2. Find matching skills

    matching_skills = find_matching_skills(
        required_skills,
        github_skills,
    )

    # 3. Find missing skills

    missing_skills = find_missing_skills(
        required_skills,
        github_skills,
    )

    # 4. Repository analysis

    repository_analysis = []

    for repository in repositories:

        repository_analysis.append(
            analyze_repository_alignment(
                repository,
                required_skills,
            )
        )

    # 5. README analysis

    repositories_without_readme = [
        repository["name"]
        for repository in repositories
        if not repository.get(
            "has_readme",
            False
        )
    ]

    # 6. Topics analysis

    repositories_without_topics = [
        repository["name"]
        for repository in repositories
        if not repository.get(
            "topics",
            []
        )
    ]

    # 7. Return alignment data

    return {
        "target_role": target_role,

        "github_username": profile.get(
            "username",
            "Not specified"
        ),

        "github_skills": github_skills,

        "matching_skills": matching_skills,

        "missing_skills": missing_skills,

        "repositories_without_readme": (
            repositories_without_readme
        ),

        "repositories_without_topics": (
            repositories_without_topics
        ),

        "repository_analysis": repository_analysis,
    }