from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

banco_url = DATABASE_URL

engine = create_engine(banco_url)

SessionLocal = sessionmaker(bind=engine)

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

Base = declarative_base()