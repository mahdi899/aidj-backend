from fastapi import APIRouter
from app.schemas.auth import AuthSession, TelegramAuthInput, RefreshInput

router = APIRouter()

@router.post("/telegram", response_model=AuthSession)
def auth_telegram(payload: TelegramAuthInput):
    # NOTE: Placeholder implementation
    return AuthSession(access_token="dev_access", refresh_token="dev_refresh")

@router.post("/refresh", response_model=AuthSession)
def refresh_token(payload: RefreshInput):
    # NOTE: Placeholder implementation
    return AuthSession(access_token="dev_access_new", refresh_token=payload.refresh_token)
