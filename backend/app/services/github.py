# HireCraft - GitHub Strategy Service

from app.schemas.github import GitHubPlan


# Temporary deterministic role → technology mapping.
#
# This is intentionally deterministic for now.
# Later this can be enhanced using the AIService.

ROLE_TECHNOLOGIES = {

    "backend developer": [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "REST API",
        "Git",
    ],

    "python developer": [
        "Python",
        "FastAPI",
        "Django",
        "SQL",
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
        "FastAPI",
        "PostgreSQL",
        "Git",
    ],

    "software engineer": [
        "Python",
        "SQL",
        "REST API",
        "Git",
        "Docker",
    ],

    "data analyst": [
        "Python",
        "SQL",
        "Pandas",
        "Excel",
        "Power BI",
    ],

    "data engineer": [
        "Python",
        "SQL",
        "PostgreSQL",
        "ETL",
        "Docker",
    ],

    "machine learning engineer": [
        "Python",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "Scikit-learn",
    ],

    "ai engineer": [
        "Python",
        "Machine Learning",
        "FastAPI",
        "REST API",
        "Git",
    ],
}


KNOWN_TECHNOLOGIES = [
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
    "scikit-learn",
]


def extract_technologies_from_job_description(
    job_description: str,
) -> list[str]:
    """
    Extract technologies explicitly mentioned
    in the job description.

    No existing GitHub information is used.
    """

    text = job_description.lower()

    found_technologies = []

    for technology in KNOWN_TECHNOLOGIES:

        if technology in text:

            formatted = technology.title()

            if formatted not in found_technologies:
                found_technologies.append(formatted)

    return found_technologies


def get_role_technologies(
    target_role: str,
) -> list[str]:
    """
    Get default technologies for a target role.

    Used when the user provides only a target role.
    """

    role = target_role.strip().lower()

    return ROLE_TECHNOLOGIES.get(
        role,
        []
    )


def detect_target_role(
    job_description: str,
) -> str | None:
    """
    Detect a target role from a job description.
    """

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

            return title.title()

    return None


def generate_github_plan(
    target_role: str | None = None,
    job_description: str | None = None,
) -> GitHubPlan:
    """
    Generate a complete GitHub strategy using ONLY:

    - target_role
    OR
    - job_description

    No existing GitHub profile,
    repositories or contribution history are used.
    """

    # 1. Determine target role

    if job_description:

        job_description = job_description.strip()

        detected_role = detect_target_role(
            job_description
        )

        if detected_role:

            target_role = detected_role

        elif target_role:

            target_role = target_role.strip()

        else:

            target_role = "Not specified"

    elif target_role:

        target_role = target_role.strip()

    else:

        target_role = "Not specified"


    # 2. Determine technologies

    if job_description:

        technologies = (
            extract_technologies_from_job_description(
                job_description
            )
        )

    else:

        technologies = get_role_technologies(
            target_role
        )


    # 3. Repository Strategy

    repository_strategy = [
        f"Build repositories that demonstrate {target_role} skills.",
        "Keep repositories focused on practical and career-relevant projects.",
        "Maintain clean and organized repository structures.",
        "Use meaningful commit messages and maintain development history.",
        "Prioritize repositories that demonstrate the required technologies.",
    ]


    # 4. Project Recommendations

    project_recommendations = [
        f"Build a beginner-to-intermediate project related to {target_role}.",
        "Build a project that solves a practical real-world problem.",
        "Create a project demonstrating multiple required technologies.",
        "Build one project that demonstrates API or application development.",
        "Create a project that can be explained clearly during interviews.",
    ]


    # Add technology-specific project recommendations

    if technologies:

        for technology in technologies[:5]:

            project_recommendations.append(
                f"Build a project demonstrating practical use of {technology}."
            )


    # 5. Technology Focus

    technology_focus = technologies


    # 6. Repository Naming Strategy

    repository_naming_strategy = [
        "Use short and descriptive repository names.",
        "Make the repository name clearly communicate the project purpose.",
        "Avoid generic names such as test-project or project1.",
        "Use consistent naming conventions across repositories.",
        "Include the main technology or purpose when useful.",
    ]


    # 7. README Strategy

    readme_strategy = [
        "Start every important repository with a professional README.",
        "Explain the project purpose and problem being solved.",
        "Document the technologies and frameworks used.",
        "Explain the main features of the project.",
        "Include installation and setup instructions.",
        "Explain how to run the project locally.",
        "Add screenshots or demonstrations when useful.",
        "Document important technical decisions.",
    ]


    # 8. GitHub Activity Strategy

    github_activity_strategy = [
        "Maintain consistent GitHub activity.",
        "Commit code regularly while developing projects.",
        "Use meaningful commit messages.",
        "Push completed features instead of only uploading final code.",
        "Keep repositories updated as skills improve.",
        "Document important project milestones.",
    ]


    # 9. Contribution Strategy

    contribution_strategy = [
        "Explore open-source repositories related to the target role.",
        "Start with documentation and beginner-friendly issues.",
        "Contribute bug fixes or small improvements when possible.",
        "Review issues related to the required technologies.",
        "Gradually work toward larger open-source contributions.",
    ]


    # 10. Keyword Strategy

    keyword_strategy = [
        f"Use '{target_role}' naturally in relevant repository descriptions.",
        "Use important technical skills in repository descriptions.",
        "Include relevant technologies in README files.",
        "Use consistent technology terminology across repositories.",
        "Use project descriptions that clearly communicate technical skills.",
    ]


    # 11. Return complete GitHub Plan

    return GitHubPlan(

        target_role=target_role,

        repository_strategy=repository_strategy,

        project_recommendations=project_recommendations,

        technology_focus=technology_focus,

        repository_naming_strategy=repository_naming_strategy,

        readme_strategy=readme_strategy,

        github_activity_strategy=github_activity_strategy,

        contribution_strategy=contribution_strategy,

        keyword_strategy=keyword_strategy,
    )