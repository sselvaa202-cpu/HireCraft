# HireCraft - GitHub Repository Evidence

import base64
import json
from typing import Any

from app.services.github_api import (
    get_repository_contents,
    get_repository_file,
)


TECHNOLOGY_FILES = {
    "requirements.txt": "Python dependencies",
    "requirements-dev.txt": "Python development dependencies",
    "pyproject.toml": "Python project configuration",
    "package.json": "JavaScript dependencies",
    "Dockerfile": "Docker configuration",
    "docker-compose.yml": "Docker Compose configuration",
    "docker-compose.yaml": "Docker Compose configuration",
    "alembic.ini": "Alembic database migration configuration",
}


DEPENDENCY_TECHNOLOGIES = {
    "fastapi": "FastAPI",
    "sqlalchemy": "SQLAlchemy",
    "alembic": "Alembic",
    "pydantic": "Pydantic",
    "pydantic-settings": "Pydantic Settings",
    "httpx": "HTTPX",
    "uvicorn": "Uvicorn",
    "requests": "Requests",
    "django": "Django",
    "flask": "Flask",
    "psycopg": "PostgreSQL",
    "psycopg2": "PostgreSQL",
    "psycopg2-binary": "PostgreSQL",
    "asyncpg": "PostgreSQL",
    "redis": "Redis",
    "celery": "Celery",
    "pytest": "Pytest",
    "numpy": "NumPy",
    "pandas": "Pandas",
    "scikit-learn": "Scikit-learn",
    "openai": "OpenAI API",
    "langchain": "LangChain",
    "chromadb": "ChromaDB",
    "react": "React",
    "react-dom": "React",
    "next": "Next.js",
    "express": "Express",
}


def decode_github_file_content(
    file_data: dict[str, Any],
) -> str:
    """
    Decode GitHub API Base64 file content.
    """

    content = file_data.get("content")

    if not content:
        return ""

    if file_data.get("encoding") != "base64":
        return content

    try:
        decoded = base64.b64decode(content)
        return decoded.decode(
            "utf-8",
            errors="ignore",
        )

    except Exception:
        return ""


def get_dependency_name(
    line: str,
) -> str | None:
    """
    Extract a dependency name from a requirements-style line.
    """

    line = line.strip()

    if not line:
        return None

    if line.startswith("#"):
        return None

    if line.startswith("-"):
        return None

    dependency = (
        line
        .split("==", 1)[0]
        .split(">=", 1)[0]
        .split("<=", 1)[0]
        .split("~=", 1)[0]
        .split(">", 1)[0]
        .split("<", 1)[0]
        .split("[", 1)[0]
        .strip()
        .lower()
    )

    return dependency or None


def detect_dependency_evidence(
    file_path: str,
    content: str,
) -> list[dict[str, str]]:
    """
    Detect technologies from actual file contents.
    """

    evidence = []

    file_name = file_path.split("/")[-1].lower()

    if file_name in {
        "requirements.txt",
        "requirements-dev.txt",
    }:

        for line in content.splitlines():

            dependency = get_dependency_name(line)

            if not dependency:
                continue

            technology = DEPENDENCY_TECHNOLOGIES.get(
                dependency
            )

            if technology:
                evidence.append(
                    {
                        "file": file_path,
                        "technology": technology,
                        "evidence": (
                            f"Dependency '{dependency}' "
                            f"found in {file_path}."
                        ),
                    }
                )

    elif file_name == "package.json":

        try:
            package_data = json.loads(content)

        except json.JSONDecodeError:
            return evidence

        dependencies = {}

        dependencies.update(
            package_data.get(
                "dependencies",
                {},
            )
        )

        dependencies.update(
            package_data.get(
                "devDependencies",
                {},
            )
        )

        for dependency in dependencies:

            technology = (
                DEPENDENCY_TECHNOLOGIES.get(
                    dependency.lower()
                )
            )

            if technology:
                evidence.append(
                    {
                        "file": file_path,
                        "technology": technology,
                        "evidence": (
                            f"Dependency '{dependency}' "
                            f"found in {file_path}."
                        ),
                    }
                )

    elif file_name == "alembic.ini":

        if "[alembic]" in content:

            evidence.append(
                {
                    "file": file_path,
                    "technology": "Alembic",
                    "evidence": (
                        "Alembic configuration "
                        "found in alembic.ini."
                    ),
                }
            )

    elif file_name in {
        "dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
    }:

        if content.strip():

            evidence.append(
                {
                    "file": file_path,
                    "technology": "Docker",
                    "evidence": (
                        f"Docker configuration "
                        f"found in {file_path}."
                    ),
                }
            )

    return evidence


def find_technology_files(
    owner: str,
    repository: str,
    path: str = "",
    max_depth: int = 3,
) -> list[str]:
    """
    Recursively find technology/configuration files.
    """

    if path.count("/") >= max_depth:
        return []

    try:
        contents = get_repository_contents(
            owner,
            repository,
        ) if not path else get_repository_contents(
            owner,
            repository,
        )

    except Exception:
        return []

    # The current GitHub API function does not accept a path.
    # Therefore this function is intentionally not used
    # for recursive traversal yet.
    return []


def inspect_directory(
    owner: str,
    repository: str,
    path: str = "",
    depth: int = 0,
    max_depth: int = 3,
) -> tuple[list[str], list[str]]:
    """
    Recursively inspect repository directories.

    Returns:
        files
        technology_files
    """

    if depth > max_depth:
        return [], []

    try:

        if path:
            from app.services.github_api import github_request

            contents = github_request(
                f"/repos/{owner}/{repository}/contents/{path}"
            )

        else:
            contents = get_repository_contents(
                owner,
                repository,
            )

    except Exception:
        return [], []

    files = []
    technology_files = []

    technology_file_names = {
        name.lower()
        for name in TECHNOLOGY_FILES
    }

    for item in contents:

        item_type = item.get("type")
        item_path = item.get("path", "")
        item_name = item.get("name", "")

        if item_type == "file":

            files.append(item_path)

            if item_name.lower() in technology_file_names:

                technology_files.append(
                    item_path
                )

        elif item_type == "dir":

            nested_files, nested_technology_files = (
                inspect_directory(
                    owner,
                    repository,
                    item_path,
                    depth + 1,
                    max_depth,
                )
            )

            files.extend(nested_files)

            technology_files.extend(
                nested_technology_files
            )

    return files, technology_files


def detect_repository_evidence(
    username: str,
    repository: str,
) -> dict[str, Any]:
    """
    Inspect the repository recursively and detect
    technology-related evidence.
    """

    files, technology_files = (
        inspect_directory(
            username,
            repository,
        )
    )

    technology_evidence = []

    for file_path in technology_files:

        try:

            file_data = get_repository_file(
                username,
                repository,
                file_path,
            )

            content = decode_github_file_content(
                file_data
            )

            detected = detect_dependency_evidence(
                file_path,
                content,
            )

            technology_evidence.extend(
                detected
            )

        except Exception:
            continue

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
        {},
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