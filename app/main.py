from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.routes import auth, moods, remix, users, tracks

app = FastAPI(title="AI DJ API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/healthz")
def healthz():
    return {"ok": True}

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(moods.router, prefix="/api/v1/mood", tags=["mood"])
app.include_router(remix.router, prefix="/api/v1/remix", tags=["remix"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(tracks.router, prefix="/api/v1/tracks", tags=["tracks"])
