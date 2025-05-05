from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime, timezone
from .database import Base

# Creation of sqlalchemy models that represent db tables

# Creates the class in sqlalchemy
class Movie(Base):
    # Indicates the corresponding table in the db
    __tablename__ = "movies"

    # Creates the corresponding columns in the Movie class
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    release_date = Column(String, nullable=False)
    watched = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    status = Column(String, default="active")

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String, nullable=False)
    endpoint = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))