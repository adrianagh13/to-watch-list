from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Defines url for sqlite database, indicates where to find db file
DATABASE_URL = "sqlite:///./test.db"

# Creates engine that connects the FastAPI app to the database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Creates a Session to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creates a Base class for sqlalchemy to manage models and map them to db tables
Base = declarative_base()