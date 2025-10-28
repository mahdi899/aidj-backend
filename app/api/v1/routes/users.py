from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def me():
    return {"id": 1, "email": "user@example.com", "display_name": "Demo"}
