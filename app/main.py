from fastapi import FastAPI
from app.database import engine, Base
from app import models, crud, schemas

app = FastAPI()

# 🔥 CREA TABLAS AUTOMÁTICAMENTE
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "GB Paradise API 🚀"}


@app.get("/offers")
def read_offers():
    return crud.get_offers()


@app.get("/reservations")
def read_reservations():
    return crud.get_reservations()


@app.post("/reservations")
def add_reservation(reservation: schemas.ReservationSchema):
    return crud.create_reservation(reservation)