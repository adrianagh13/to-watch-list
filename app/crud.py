from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timezone

# Method for adding a movie
def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# Method for retrieving all movies
def read_movie_list(db: Session):
    return db.query(models.Movie).filter(models.Movie.status == "active").all()

# Method for retrieving a specific movie with an id
def read_movie(db: Session, movie_id: int):
  return db.query(models.Movie).filter(models.Movie.id == movie_id, models.Movie.status == "active").first()

# Method for updating movie details
def update_movie(db: Session, movie_id: int, data: schemas.MovieUpdate):
  movie = read_movie(db, movie_id)
  if not movie:
    return None
  for key, value in data.dict(exclude_unset=True).items():
    setattr(movie, key, value)
  movie.updated_at = datetime.now(timezone.utc)
  db.commit()
  return movie

# Method for marking a movie as watched
def mark_watched(db: Session, movie_id: int):
  movie = read_movie(db, movie_id)
  if not movie:
    return None
  movie.watched = True
  movie.updated_at = datetime.now(timezone.utc)
  db.commit()
  return movie

# Method for deleting a movie
def delete_movie(db: Session, movie_id: int):
  movie = read_movie(db, movie_id)
  if not movie:
    return None
  movie.status = "deleted"
  movie.updated_at = datetime.now(timezone.utc)
  db.commit()
  return movie