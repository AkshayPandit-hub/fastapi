import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# load_dotenv()

database_url = os.getenv("DATABASE_URL")

engine = create_engine(database_url,echo= True)

try:
    with engine.connect() as conn:
        print("database connected successfully")
except Exception:
    print("Database connection error")

SessionLocal = sessionmaker(bind=engine, autoflush=False)


