# HireCraft - Job Analysis Prompt

from app.ai.prompts.system import SYSTEM_PROMPT


def build_job_analysis_prompt(job_description: str) -> str:
    """
    Build the prompt used to analyze a job description.
    """

    return f"""
{SYSTEM_PROMPT}

Analyze the following job description.

JOB DESCRIPTION:
----------------
{job_description}
----------------

Extract:

1. Actual job title
2. Required technical and professional skills
3. Important responsibilities
4. Required experience level
5. Required education

Do not invent information.

If information is not present, use:
"Not specified"

Return ONLY valid JSON.

Use exactly this structure:

{{
    "job_title": "string",
    "required_skills": [],
    "responsibilities": [],
    "experience_level": "string",
    "education": "string"
}}

Rules:

- required_skills must be an array of strings.
- responsibilities must be an array of strings.
- Do not include explanations outside JSON.
"""