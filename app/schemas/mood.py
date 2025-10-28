from pydantic import BaseModel
from typing import List

class MoodAnalyzeText(BaseModel):
    text: str

class SuggestedTrack(BaseModel):
    id: int | None = None
    title: str
    artist: str

class MoodAnalysis(BaseModel):
    mood_label: str
    intensity: int
    suggested_tracks: List[SuggestedTrack] = []
