from pydantic import BaseModel

class AuthSession(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TelegramAuthInput(BaseModel):
    init_data: str

class RefreshInput(BaseModel):
    refresh_token: str
