from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.db.base import Base

class RemixJob(Base):
    __tablename__ = "remix_jobs"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    input_a_id: Mapped[int] = mapped_column(Integer, ForeignKey("tracks.id"))
    input_b_id: Mapped[int] = mapped_column(Integer, ForeignKey("tracks.id"))
    status: Mapped[str] = mapped_column(String(16), default="PENDING")
    params: Mapped[str] = mapped_column(String(2048), default="{}")
    result_url: Mapped[str] = mapped_column(String(1024), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
