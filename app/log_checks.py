from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Log

# Creates an instance of the APIRouter class
log_router = APIRouter()

# Creates a db session
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# Queries the Log table and retrieves all logs
@log_router.get("/logs")
def get_logs(db: Session = Depends(get_db)):
  return db.query(Log).all()
