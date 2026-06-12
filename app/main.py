from fastapi import FastAPI
from app.database import engine, Base
from app import models, crud, schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)


# ======================
# HOME
# ======================
@app.get("/")
def home():
    return {"message": "GB Paradise API 🚀"}


# ======================
# OFFERS
# ======================
@app.get("/offers")
def read_offers():
    return crud.get_offers()


# ======================
# RESERVATIONS
# ======================
@app.get("/reservations")
def read_reservations():
    return crud.get_reservations()


@app.post("/reservations")
def add_reservation(reservation: schemas.ReservationSchema):
    return crud.create_reservation(reservation)


from app.seed import seed_offers

@app.on_event("startup")
def startup():
    seed_offers()