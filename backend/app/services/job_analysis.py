# HireCraft - Job Analysis Service

import re

from app.schemas.job import JobRequirement

def normalize_skills(skills: list[str]) -> list[str]:
    """
    Normalize extracted skills and remove obvious duplicates.
    """

    normalized = []

    for skill in skills:

        skill = skill.strip().lower()

        if not skill:
            continue

        # Normalize common variations
        skill_aliases = {
            "rest apis": "rest api",
            "rest api": "rest api",
            "apis": "api",
            "postgres": "postgresql",
            "js": "javascript",
            "ts": "typescript",
        }

        skill = skill_aliases.get(
            skill,
            skill
        )

        if skill not in normalized:
            normalized.append(skill)

    # If REST API exists, generic API is redundant
    if "rest api" in normalized and "api" in normalized:
        normalized.remove("api")

    return normalized

def analyze_job_description(job_description: str) -> JobRequirement:
    """
    Analyze a job description and extract structured requirements.
    """

    # Normalize job description

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
        "excel",
        "power bi",
    ]

    required_skills = []

    for skill in skill_keywords:

        pattern = rf"\b{re.escape(skill)}\b"

        if re.search(pattern, text):
            required_skills.append(skill)

    required_skills = normalize_skills(
        required_skills
)

    # Responsibilities
    # Phase 4.3

    responsibilities = []

    responsibility_verbs = [
        "develop",
        "design",
        "build",
        "maintain",
        "implement",
        "test",
        "debug",
        "deploy",
        "integrate",
        "write",
        "create",
        "manage",
        "optimize",
    ]

    # Split the original job description into sentences
    sentences = re.split(
        r"[.!?\n]+",
        job_description
    )

    for sentence in sentences:

        sentence = sentence.strip()

        if not sentence:
            continue

        sentence_lower = sentence.lower()

        # Check whether the sentence contains
        # a responsibility-related verb
        contains_responsibility = any(
            re.search(
                rf"\b{verb}\b",
                sentence_lower
            )
            for verb in responsibility_verbs
        )

        if contains_responsibility:

            # Avoid adding extremely long paragraphs
            if len(sentence.split()) <= 30:

                # Remove common bullet characters
                sentence = re.sub(
                    r"^[\-\*\•\▪\●]+\s*",
                    "",
                    sentence
                )

                # Avoid duplicates
                if sentence not in responsibilities:

                    responsibilities.append(sentence)

    # Experience detection

    experience_level = "Not specified"

    if (
        "fresher" in text
        or "freshers" in text
        or "entry level" in text
        or "entry-level" in text
    ):
        experience_level = "Fresher"

    elif (
        "1 year" in text
        or "1+ year" in text
        or "1+ years" in text
    ):
        experience_level = "1+ year"

    elif (
        "2 years" in text
        or "2+ years" in text
    ):
        experience_level = "2+ years"

    elif (
        "3 years" in text
        or "3+ years" in text
    ):
        experience_level = "3+ years"

    # Education detection

    education = "Not specified"

    if (
        "bachelor" in text
        or "b.com" in text
        or "b.tech" in text
        or "b.e" in text
    ):
        education = "Bachelor's degree"

    elif (
        "master" in text
        or "m.tech" in text
        or "m.com" in text
        or "m.e" in text
    ):
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

    # Create structured JobRequirement object

    return JobRequirement(
        job_title=job_title,
        required_skills=required_skills,
        responsibilities=responsibilities,
        experience_level=experience_level,
        education=education,
    )
