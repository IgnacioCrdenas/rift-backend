from fastapi import FastAPI
from .core.config import settings

app = FastAPI()

@app.get("/env/")
async def read_env():
    return {
        "database_url": settings.database_url,
        "firebase_credentials": settings.firebase_credentials,
        "firebase_storage_bucket": settings.firebase_storage_bucket,
        "debug": settings.debug,
        "environment": settings.environment,
    }