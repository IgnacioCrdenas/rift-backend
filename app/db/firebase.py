"""
Firebase configuration and utilities for Realtime Database and Storage.
"""

import firebase_admin
from firebase_admin import credentials, db, storage
from app.core.config import settings

# Initialize Firebase app with credentials and database URL
cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
firebase_admin.initialize_app(cred, {
    "databaseURL": settings.DATABASE_URL,
    "storageBucket": settings.FIREBASE_STORAGE_BUCKET
})

def save_data(reference: str, data: dict) -> str:
    """
    Save data to Firebase Realtime Database.

    Args:
        reference (str): Database reference (e.g., "pages").
        data (dict): Data to save.

    Returns:
        str: Key of the newly created data.
    """
    ref = db.reference(reference)
    return ref.push(data).key

def get_data(reference: str) -> dict:
    """
    Retrieve data from Firebase Realtime Database.

    Args:
        reference (str): Database reference (e.g., "pages/{id}").

    Returns:
        dict: Data retrieved or None if not found.
    """
    ref = db.reference(reference)
    return ref.get()

def upload_file(bucket_name: str, source_file: str, destination_blob: str) -> str:
    """
    Upload a file to Firebase Storage.

    Args:
        bucket_name (str): Name of the storage bucket.
        source_file (str): Local path to the file.
        destination_blob (str): Destination path in the bucket.

    Returns:
        str: Public URL of the uploaded file.
    """
    bucket = storage.bucket(bucket_name)
    blob = bucket.blob(destination_blob)
    blob.upload_from_filename(source_file)
    return blob.public_url