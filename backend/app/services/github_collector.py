# HireCraft - GitHub Profile & Repository Collector

from app.services.github_api import (
    extract_github_username,
    get_github_profile,
    get_github_repositories,
    get_repository_languages,
    get_repository_contents,
    get_repository_readme,
)


def collect_github_profile(
    github_url: str,
) -> dict:
    """
    Collect public GitHub profile and repository information.

    This service only collects data.
    It does NOT perform AI analysis.
    """

    # 1. Extract username

    username = extract_github_username(
        github_url
    )

    # 2. Get profile

    profile = get_github_profile(
        username
    )

    # 3. Get repositories

    repositories = get_github_repositories(
        username
    )

    collected_repositories = []

    # 4. Collect repository information

    for repository in repositories:

        repo_name = repository["name"]

        # Languages
        try:
            language_data = get_repository_languages(
                username,
                repo_name,
            )

            languages = list(
                language_data.keys()
            )

        except Exception:
            languages = []

        # Topics
        topics = repository.get(
            "topics",
            []
        )

        # README
        try:
            readme = get_repository_readme(
                username,
                repo_name,
            )

            has_readme = readme is not None

        except Exception:
            has_readme = False

        # Repository structure
        try:
            contents = get_repository_contents(
                username,
                repo_name,
            )

            structure = [
                item.get("name")
                for item in contents
            ]

        except Exception:
            structure = []

        collected_repositories.append(
            {
                "name": repo_name,

                "description": repository.get(
                    "description"
                ),

                "html_url": repository.get(
                    "html_url"
                ),

                "languages": languages,

                "topics": topics,

                "stars": repository.get(
                    "stargazers_count",
                    0,
                ),

                "forks": repository.get(
                    "forks_count",
                    0,
                ),

                "updated_at": repository.get(
                    "updated_at"
                ),

                "has_readme": has_readme,

                "structure": structure,
            }
        )

    # 5. Return collected GitHub data

    return {
        "profile": {
            "username": profile.get(
                "login"
            ),

            "name": profile.get(
                "name"
            ),

            "bio": profile.get(
                "bio"
            ),

            "public_repositories": profile.get(
                "public_repos",
                0,
            ),

            "followers": profile.get(
                "followers",
                0,
            ),

            "following": profile.get(
                "following",
                0,
            ),

            "profile_url": profile.get(
                "html_url"
            ),
        },

        "repositories": collected_repositories,
    }