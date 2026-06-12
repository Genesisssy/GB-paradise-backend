from fastapi import FastAPI
from app.database import engine, Base
from app import models

app = FastAPI()

# crea tablas en MySQL automáticamente
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "GB Paradise API running 🚀"}