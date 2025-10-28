from fastapi import APIRouter, UploadFile, File, Form
from app.schemas.mood import MoodAnalyzeText, MoodAnalysis
from app.services.mood_analyzer import analyze_text

router = APIRouter()

@router.post("/analyze", response_model=MoodAnalysis)
async def analyze_mood(
    text: str | None = Form(default=None),
    voice: UploadFile | None = File(default=None)
):
    # Placeholder: voice ignored; use text heuristic
    if text is None:
        text = "calm"
    label, intensity, suggested = analyze_text(text)
    return {"mood_label": label, "intensity": intensity, "suggested_tracks": suggested}
