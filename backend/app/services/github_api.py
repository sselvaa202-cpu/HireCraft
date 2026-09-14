# HireCraft - GitHub API Service

import re
import requests


GITHUB_API = "https://api.github.com"


def extract_github_username(
    github_url: str,
) -> str:

    github_url = github_url.strip().rstrip("/")

    pattern = r"github\.com/([^/]+)"

    match = re.search(
        pattern,
        github_url,
        re.IGNORECASE,
    )

    if not match:
        raise ValueError(
            "Invalid GitHub profile URL."
        )

    return match.group(1)


def github_request(
    endpoint: str,
):

    response = requests.get(
        f"{GITHUB_API}{endpoint}",
        timeout=10,
        headers={
            "Accept": "application/vnd.github+json"
        },
    )

    response.raise_for_status()

    return response.json()


def get_github_profile(
    username: str,
):

    return github_request(
        f"/users/{username}"
    )


def get_github_repositories(
    username: str,
):

    return github_request(
        f"/users/{username}/repos?per_page=100&sort=updated"
    )


def get_repository_languages(
    owner: str,
    repository: str,
):

    return github_request(
        f"/repos/{owner}/{repository}/languages"
    )


def get_repository_contents(
    owner: str,
    repository: str,
):

    return github_request(
        f"/repos/{owner}/{repository}/contents"
    )

def get_repository_file(
    owner: str,
    repository: str,
    file_path: str,
):
    """
    Get the content of a specific file from a GitHub repository.
    """

    return github_request(
        f"/repos/{owner}/{repository}/contents/{file_path}"
    )


def get_repository_readme(
    owner: str,
    repository: str,
):

    response = requests.get(
        f"{GITHUB_API}/repos/{owner}/{repository}/readme",
        timeout=10,
        headers={
            "Accept": "application/vnd.github+json"
        },
    )

    if response.status_code == 404:
        return None

    response.raise_for_status()

    return response.json()