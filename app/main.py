from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app import models, schemas, crud
from .database import engine, SessionLocal
from .logger import log_request
from .log_checks import log_router
from .health_checks import health_router
from sqlalchemy.orm import Session

# Creates the tables of the database based on the defined models
models.Base.metadata.create_all(bind=engine)
# Initialize the application using FastAPI class
app = FastAPI()
# Creates a middleware for log requests
app.middleware("http")(log_request)
# Registers routes to verify the state of the system
app.include_router(health_router)
# Registers routes to query registered logs
app.include_router(log_router)

# Creates a db Session for each request to interact with the database/endpoints
# Each session is a connection to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------------------
# API Endpoints for movie management
# ----------------------------------------

# Endpoint for adding a movie, response model indicates the type of data
@app.post("/movies/", response_model=schemas.MovieOut, status_code=201)
def add_movie(movie:schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

# Endpoint for retrieving all movies
@app.get("/movies/", response_model=list[schemas.MovieOut])
def list_movies(db: Session = Depends(get_db)):
    return crud.read_movie_list(db)

# Endpoint for retrieving details of a specific movie
@app.get("/movies/{movie_id}", response_model=schemas.MovieOut)
def specific_movie(movie_id: int, db: Session = Depends(get_db)):
  movie = crud.read_movie(db, movie_id)
  if not movie:
    raise HTTPException(status_code=404, detail="Movie not found")
  return movie

# Endpoint for updating movie details
@app.put("/movies/{movie_id}", response_model=schemas.MovieOut)
def update_movie(movie_id: int, update: schemas.MovieUpdate, db: Session = Depends(get_db)):
  movie = crud.update_movie(db, movie_id, update)
  if not movie:
    raise HTTPException(status_code=404, detail="Movie not found")
  return movie

# Endpoint for marking a movie as watched
@app.patch("/movies/{movie_id}/watched", response_model=schemas.MovieOut)
def mark_as_watched(movie_id: int, db: Session = Depends(get_db)):
  movie = crud.mark_watched(db, movie_id)
  if not movie:
    raise HTTPException(status_code=404, detail="Movie not found")
  return movie

# Endpoint for deleting a movie
@app.delete("/movies/{movie_id}", response_model=schemas.MovieOut)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
  movie = crud.delete_movie(db, movie_id)
  if not movie:
    raise HTTPException(status_code=404, detail="Movie not found")
  return movie