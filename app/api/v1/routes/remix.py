from fastapi import APIRouter
from app.schemas.remix import RemixCreate, RemixJobOut
from app.services import remix_engine

router = APIRouter()

@router.post("", response_model=RemixJobOut)
def create_remix(payload: RemixCreate):
    job_id = remix_engine.submit_job(**payload.model_dump())
    return {"job_id": job_id, "status": "PENDING"}

@router.get("/{job_id}", response_model=RemixJobOut)
def get_remix(job_id: int):
    s = remix_engine.get_job_status(job_id)
    return {"job_id": job_id, **s}
