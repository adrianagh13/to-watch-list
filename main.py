from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ToWatchList API is working!"}