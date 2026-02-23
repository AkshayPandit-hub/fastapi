import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# load_dotenv()

database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set. Please configure it in your Azure App Service settings or .env file.")
print("🔍 DATABASE_URL in Azure:", database_url)
engine = create_engine(database_url,echo= True)

try:
    with engine.connect() as conn:
        print("database connected successfully")
except Exception:
    print("Database connection error")

SessionLocal = sessionmaker(bind=engine, autoflush=False)


