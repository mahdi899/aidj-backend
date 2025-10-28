from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.db.base import Base

class MoodAnalysis(Base):
    __tablename__ = "mood_analyses"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    text: Mapped[str] = mapped_column(String(2048), default="")
    mood_label: Mapped[str] = mapped_column(String(64))
    intensity: Mapped[int] = mapped_column(Integer, default=0)
    suggested_tracks: Mapped[str] = mapped_column(String(4096), default="[]")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
