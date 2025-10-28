from pydantic import BaseModel
from typing import Optional, Literal

class RemixCreate(BaseModel):
    input_a_id: int
    input_b_id: int
    style: Optional[str] = None
    pitch_a: Optional[int] = 0
    pitch_b: Optional[int] = 0
    segment_sec: Optional[int] = 10

class RemixJobOut(BaseModel):
    job_id: int
    status: Literal["PENDING","RUNNING","DONE","FAILED"]
    result_url: Optional[str] = None
