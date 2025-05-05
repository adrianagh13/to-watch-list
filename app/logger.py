from fastapi import Request
from .database import SessionLocal
from .models import Log
from datetime import datetime, timezone

# Creates a middleware as an async function for http requests
async def log_request(request: Request, call_next):
  response = await call_next(request)
  db = SessionLocal()# opens a db session
  log = Log( # creates a new register of the log
    method=request.method,
    endpoint=request.url.path,
    timestamp=datetime.now(timezone.utc)
  )
  db.add(log)
  db.commit()
  db.close()

  return response