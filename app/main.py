from fastapi import FastAPI
from app.db.connection.database import get_db

app = FastAPI()

@app.get("/")
def read_root():
    get_db()
    return {"Hello": "World From FastAPI v2 dd"}