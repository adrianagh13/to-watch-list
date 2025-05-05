from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Creation of pydantic schemas used for data validation when working with http requests and responses

# Creates base schema that defines common fields on other schemas, DRY principle
class MovieBase(BaseModel):
    name: str
    release_date: str

# Creates schema for the creation of a new movie, POST req
class MovieCreate(MovieBase):
    pass # Passes because it inherits MovieBase properties only

# Creates schema for the update of movie details, PATCH/PUT req
class MovieUpdate(BaseModel):
    name: Optional[str] = None 
    release_date: Optional[str] = None

# Defines the data returned, GET responses
class MovieOut(MovieBase): # Inheritance
    id: int
    watched: bool
    created_at: datetime
    updated_at: datetime
    status: str

# Accepts ORM models instances rather than just dicts
    class Config:
        from_attributes = True
