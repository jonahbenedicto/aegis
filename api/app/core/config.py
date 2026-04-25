import os
from datetime import timedelta
from dotenv import load_dotenv
 
load_dotenv()
 
SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is not set")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")
 
ALGORITHM = "HS256"
 
ACCESS_TOKEN_EXPIRE = timedelta(minutes=15)
REFRESH_TOKEN_EXPIRE = timedelta(days=7)
 