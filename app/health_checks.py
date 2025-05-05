from fastapi import APIRouter

# Creates an instance of the APIRouter class
health_router = APIRouter()

# Adds a path operation fot the /health endpoint
@health_router.get("/health")
def check():
  return {"status": "ok"}
