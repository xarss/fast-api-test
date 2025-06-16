import os

from dotenv import load_dotenv

load_dotenv()

try:
    GOOGLE_CLIENT_ID: str = os.environ["GOOGLE_CLIENT_ID"]
    JWT_SECRET_KEY: str = os.environ["JWT_SECRET_KEY"]
    DATABASE_URL: str = os.environ["DATABASE_URL"]
except:
    raise ValueError("One or more mandatory environment values are missing.")

if(not DATABASE_URL):
    raise KeyError("Could not find DATABASE_URL in environment config.")

if not GOOGLE_CLIENT_ID:
    raise KeyError("GOOGLE_CLIENT_ID is not set in environment variables")

if not JWT_SECRET_KEY:
    raise KeyError("JWT_SECRET_KEY is not set in environment variables")