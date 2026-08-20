from pydantic import BaseModel


class SkillGap(BaseModel):
    skill: str
    priority: str


class AnalysisResult(BaseModel):
    match_percentage: float
    matched_skills: list[str]
    skill_gaps: list[SkillGap]
    strengths: list[str]
    recommendations: list[str]