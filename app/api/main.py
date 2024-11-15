from fastapi import FastAPI
from app.db.firebase import save_data, get_data

from core.config import settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is running"}

@app.post("/test-save/")
async def test_save():
    data = {"name": "Test Page", "content": "Sample content"}
    key = save_data("test_pages", data)
    return {"id": key}

@app.get("/test-get/{key}")
async def test_get(key: str):
    data = get_data(f"test_pages/{key}")
    return data

@app.get("/settings/")
def read_settings():
    return {
        "database_url": settings.DATABASE_URL,
        "firebase_credentials": settings.FIREBASE_CREDENTIALS,
        "storage_bucket": settings.FIREBASE_STORAGE_BUCKET,
        "environment": settings.ENVIRONMENT,
        "debug": settings.DEBUG
    }