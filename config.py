import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

GENERATED_FOLDER = os.path.join(BASE_DIR, "generated")

CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

DATABASE = os.path.join(BASE_DIR, "database", "documind.db")

SECRET_KEY = "documind-secret-key"