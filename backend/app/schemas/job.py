from pydantic import BaseModel


class JobRequirement(BaseModel):
    title: str
    skills: list[str]