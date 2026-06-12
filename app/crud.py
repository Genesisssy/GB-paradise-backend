from datetime import datetime

from app.models import (
    Offer,
    Reservation,
    Admin
)

from app.database import SessionLocal


# ======================
# OFFERS
# ======================

def get_offers():

    db = SessionLocal()

    try:

        now = datetime.now()

        offers = db.query(Offer).filter(
            Offer.is_active == True,
            Offer.end_date > now
        ).all()

        return offers

    finally:
        db.close()


def get_offer(offer_id: int):

    db = SessionLocal()

    try:

        return db.query(Offer).filter(
            Offer.id == offer_id
        ).first()

    finally:
        db.close()


def create_offer(data):

    db = SessionLocal()

    try:

        offer = Offer(
            **data.dict(),
            is_active=True
        )

        db.add(offer)

        db.commit()

        db.refresh(offer)

        return offer

    finally:
        db.close()


def update_offer(offer_id, data):

    db = SessionLocal()

    try:

        offer = db.query(Offer).filter(
            Offer.id == offer_id
        ).first()

        if not offer:
            return {
                "success": False,
                "message": "Oferta no encontrada"
            }

        for key, value in data.dict().items():
            setattr(offer, key, value)

        db.commit()

        db.refresh(offer)

        return offer

    finally:
        db.close()


def delete_offer(offer_id):

    db = SessionLocal()

    try:

        offer = db.query(Offer).filter(
            Offer.id == offer_id
        ).first()

        if not offer:
            return {
                "success": False,
                "message": "Oferta no encontrada"
            }

        db.delete(offer)

        db.commit()

        return {
            "success": True,
            "message": "Oferta eliminada correctamente"
        }

    finally:
        db.close()


# ======================
# ACTIVAR OFERTA
# ======================

def activate_offer(offer_id):

    db = SessionLocal()

    try:

        offer = db.query(Offer).filter(
            Offer.id == offer_id
        ).first()

        if not offer:
            return {
                "success": False,
                "message": "Oferta no encontrada"
            }

        offer.is_active = True

        db.commit()

        db.refresh(offer)

        return offer

    finally:
        db.close()


# ======================
# DESACTIVAR OFERTA
# ======================

def deactivate_offer(offer_id):

    db = SessionLocal()

    try:

        offer = db.query(Offer).filter(
            Offer.id == offer_id
        ).first()

        if not offer:
            return {
                "success": False,
                "message": "Oferta no encontrada"
            }

        offer.is_active = False

        db.commit()

        db.refresh(offer)

        return offer

    finally:
        db.close()


# ======================
# RESERVATIONS
# ======================

def get_reservations():

    db = SessionLocal()

    try:

        return db.query(Reservation).all()

    finally:
        db.close()


def create_reservation(data):

    db = SessionLocal()

    try:

        reservation = Reservation(
            **data.dict()
        )

        db.add(reservation)

        db.commit()

        db.refresh(reservation)

        return reservation

    finally:
        db.close()


# ======================
# ADMIN LOGIN
# ======================

def admin_login(data):

    db = SessionLocal()

    try:

        admin = db.query(Admin).filter(
            Admin.username == data.username
        ).first()

        if admin is None:

            return {
                "success": False,
                "message": "Usuario incorrecto"
            }

        if admin.password != data.password:

            return {
                "success": False,
                "message": "Contraseña incorrecta"
            }

        return {
            "success": True,
            "message": "Login correcto"
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

    finally:
        db.close()