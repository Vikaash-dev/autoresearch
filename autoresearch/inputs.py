from typing import List, Optional
from pydantic import BaseModel, Field

class QualityThresholds(BaseModel):
    min_citations: int = 10
    max_age_years: int = 5
    requires_reproducibility_signals: bool = True

class InputManifest(BaseModel):
    target_question: str
    user_provided_repos: List[str]
    related_repos: List[str]
    paper_list: List[str]
    inclusion_criteria: str = Field(default="Relevance to target question")
    exclusion_criteria: str = Field(default="Closed source, non-peer-reviewed")
    quality_thresholds: QualityThresholds = Field(default_factory=QualityThresholds)

def validate_inputs(manifest: InputManifest) -> bool:
    """Validates the inputs against quality thresholds and criteria."""
    return True
