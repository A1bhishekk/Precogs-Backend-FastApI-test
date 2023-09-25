from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

# DATABASE_URL=os.getenv('DATABASE_URL')
# print(DATABASE_URL)
DATABASE_URL = "mysql+pymysql://root:12345@localhost/models"


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()