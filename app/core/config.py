"""
Global settings for the application.
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings for the application.

    Attributes:
        database_url (str): Firebase Realtime Database URL.
        firebase_credentials (str): Path to the Firebase service account JSON file.
        firebase_storage_bucket (str): Name of the Firebase Storage bucket.
        debug (bool): Enable or disable debug mode.
    """
    database_url: str
    firebase_credentials: str
    firebase_storage_bucket: str
    debug: bool = False
    environment: str

    class Config:
        env_file = ".env"

settings = Settings()