# HireCraft - GitHub Repository Evidence

from typing import Any

from app.services.github_api import (
    get_repository_contents,
)


TECHNOLOGY_FILES = {
    "requirements.txt": "Python dependencies",
    "requirements-dev.txt": "Python development dependencies",
    "pyproject.toml": "Python project configuration",
    "package.json": "JavaScript dependencies",
    "Dockerfile": "Docker configuration",
    "docker-compose.yml": "Docker Compose configuration",
    "docker-compose.yaml": "Docker Compose configuration",
    "alembic.ini": "Alembic database migration",
}


def detect_repository_evidence(
    username: str,
    repository: str,
) -> dict[str, Any]:
    """
    Inspect repository structure and detect
    technology-related evidence.

    This does not use an LLM.
    """

    try:
        contents = get_repository_contents(
            username,
            repository,
        )

    except Exception:
        return {
            "repository": repository,
            "files": [],
            "technology_evidence": [],
        }

    files = []

    technology_evidence = []

    for item in contents:

        name = item.get(
            "name",
            ""
        )

        item_type = item.get(
            "type"
        )

        files.append(name)

        if (
            item_type == "file"
            and name.lower()
            in {
                key.lower()
                for key in TECHNOLOGY_FILES
            }
        ):

            for filename, description in (
                TECHNOLOGY_FILES.items()
            ):

                if name.lower() == filename.lower():

                    technology_evidence.append(
                        {
                            "file": name,
                            "evidence": description,
                        }
                    )

                    break

    return {
        "repository": repository,
        "files": files,
        "technology_evidence": technology_evidence,
    }


def collect_repository_evidence(
    github_data: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Collect repository-level evidence for
    every repository in the GitHub profile.
    """

    profile = github_data.get(
        "profile",
        {}
    )

    username = profile.get(
        "username"
    )

    repositories = github_data.get(
        "repositories",
        []
    )

    evidence = []

    if not username:
        return evidence

    for repository in repositories:

        repository_name = repository.get(
            "name"
        )

        if not repository_name:
            continue

        repository_evidence = (
            detect_repository_evidence(
                username,
                repository_name,
            )
        )

        evidence.append(
            repository_evidence
        )

    return evidence