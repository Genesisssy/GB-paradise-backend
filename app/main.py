from fastapi import FastAPI

from app.database import engine, Base
from app import crud

from app.schemas import (
    OfferCreate,
    ReservationSchema,
    AdminLogin
)

app = FastAPI()

# Crear tablas
Base.metadata.create_all(bind=engine)


# ======================
# HOME
# ======================

@app.get("/")
def home():

    return {
        "message": "GB Paradise API 🚀"
    }


# ======================
# OFFERS
# ======================

@app.get("/offers")
def get_offers():

    return crud.get_offers()


@app.get("/offers/{offer_id}")
def get_offer(offer_id: int):

    return crud.get_offer(offer_id)


@app.post("/offers")
def create_offer(
    offer: OfferCreate
):

    return crud.create_offer(
        offer
    )


@app.put("/offers/{offer_id}")
def update_offer(
    offer_id: int,
    offer: OfferCreate
):

    return crud.update_offer(
        offer_id,
        offer
    )


@app.delete("/offers/{offer_id}")
def delete_offer(
    offer_id: int
):

    return crud.delete_offer(
        offer_id
    )


# ======================
# ACTIVAR OFERTA
# ======================

@app.put("/offers/{offer_id}/activate")
def activate_offer(
    offer_id: int
):

    return crud.activate_offer(
        offer_id
    )


# ======================
# DESACTIVAR OFERTA
# ======================

@app.put("/offers/{offer_id}/deactivate")
def deactivate_offer(
    offer_id: int
):

    return crud.deactivate_offer(
        offer_id
    )


# ======================
# RESERVATIONS
# ======================

@app.get("/reservations")
def get_reservations():

    return crud.get_reservations()


@app.post("/reservations")
def create_reservation(
    reservation: ReservationSchema
):

    return crud.create_reservation(
        reservation
    )


# ======================
# ADMIN LOGIN
# ======================

@app.post("/admin/login")
def login_admin(
    admin: AdminLogin
):

    return crud.admin_login(
        admin
    )