from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "GB Paradise API running 🚀"}