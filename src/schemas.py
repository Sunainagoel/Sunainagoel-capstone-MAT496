from typing import List, Optional
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

# --- Structured Output Models ---
class SkillAnalysis(BaseModel):
    """Represents the skills extracted from a text."""
    technical_skills: List[str] = Field(description="List of specific technical tools, languages, or frameworks found.")
    soft_skills: List[str] = Field(description="List of soft skills or leadership qualities found.")
    experience_level: str = Field(description="Inferred experience level (e.g., Junior, Senior, Expert).")

class GapAnalysis(BaseModel):
    """Represents the missing skills after comparing Resume vs JD."""
    missing_technical_skills: List[str] = Field(description="Critical technical skills present in JD but missing in Resume.")
    missing_soft_skills: List[str] = Field(description="Soft skills present in JD but missing in Resume.")
    match_percentage: int = Field(description="Estimated fit percentage from 0 to 100.")

class Resource(BaseModel):
    """A learning resource found via tool calling."""
    skill: str
    resource_title: str
    url: str

# --- LangGraph State ---
class AgentState(TypedDict):
    resume_text: str
    job_description: str
    
    # State populated by nodes
    job_requirements: Optional[SkillAnalysis]
    resume_profile: Optional[SkillAnalysis]
    gap_data: Optional[GapAnalysis]
    learning_plan: List[Resource]
    final_report: str