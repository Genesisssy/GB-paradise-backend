from app.models import Offer, Reservation
from app.database import SessionLocal


# ======================
# OFFERS
# ======================
def get_offers():
    db = SessionLocal()
    try:
        offers = db.query(Offer).all()
        return offers
    finally:
        db.close()


# ======================
# RESERVATIONS
# ======================
def get_reservations():
    db = SessionLocal()
    try:
        reservations = db.query(Reservation).all()
        return reservations
    finally:
        db.close()


def create_reservation(reservation_data):
    db = SessionLocal()
    try:
        new_reservation = Reservation(**reservation_data.dict())
        db.add(new_reservation)
        db.commit()
        db.refresh(new_reservation)
        return new_reservation
    finally:
        db.close()