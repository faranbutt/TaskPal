from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from dotenv import load_dotenv
import os
load_dotenv('.env')

POSTGRES_USER:str = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER')
POSTGRES_DB:str = os.getenv('POSTGRES_DB')
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}?sslmode=require"


engine = create_engine(DATABASE_URL)
Session_Local = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

