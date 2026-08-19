from pydantic import BaseModel


class AnalysisResult(BaseModel):
    match_percentage: float
    matched_skills: list[str]
    skill_gaps: list[str]
    strengths: list[str]
    recommendations: list[str]