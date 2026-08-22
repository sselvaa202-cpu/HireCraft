# HireCraft - Job Analysis Service


def analyze_job_description(job_description: str) -> dict:
    """
    Analyze a job description and extract structured requirements.
    """

    text = job_description.lower()

    # Common technical skills
    skill_keywords = [
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
    ]

    required_skills = []

    for skill in skill_keywords:
        if skill in text:
            required_skills.append(skill)

    # Experience detection
    experience_level = "Not specified"

    if "fresher" in text or "entry level" in text:
        experience_level = "Fresher"

    elif "1 year" in text or "1+ year" in text:
        experience_level = "1+ year"

    elif "2 years" in text or "2+ years" in text:
        experience_level = "2+ years"

    elif "3 years" in text or "3+ years" in text:
        experience_level = "3+ years"

    # Education detection
    education = "Not specified"

    if "bachelor" in text or "b.com" in text or "b.tech" in text:
        education = "Bachelor's degree"

    elif "master" in text or "m.tech" in text or "m.com" in text:
        education = "Master's degree"

    # Job title detection
    job_title = "Not specified"

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

    for title in job_titles:
        if title in text:
            job_title = title.title()
            break

    return {
        "job_title": job_title,
        "required_skills": required_skills,
        "responsibilities": [],
        "experience_level": experience_level,
        "education": education,
    }