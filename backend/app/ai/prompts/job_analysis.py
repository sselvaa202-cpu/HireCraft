# HireCraft - Job Analysis Prompt


def build_job_analysis_prompt(job_description: str) -> str:
    """
    Build a structured prompt for analyzing a job description.
    """

    return f"""
You are a job description analysis assistant for HireCraft.

Analyze the following job description and extract the requirements.

JOB DESCRIPTION:
----------------
{job_description}
----------------

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

1. Extract the actual job title.
2. Extract technical and professional skills required by the job.
3. Extract important job responsibilities.
4. Extract the required experience level.
5. Extract the required education.
6. Do not invent information that is not present.
7. If information is not specified, use:
   "Not specified"
8. required_skills must be an array of strings.
9. responsibilities must be an array of strings.
10. Return JSON only.
"""