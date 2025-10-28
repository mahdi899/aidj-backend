# Placeholder for S3/MinIO utilities
from app.core.config import settings

def info():
    return {
        "endpoint": settings.S3_ENDPOINT,
        "bucket": settings.S3_BUCKET
    }
