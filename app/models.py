from sqlalchemy import Column, Integer, String, Float, Text, Date
from app.database import Base


# =========================
# TABLA: OFFERS
# =========================
class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    image = Column(String(255))
    price = Column(Float)
    old_price = Column(Float)
    rating = Column(Float)
    duration = Column(String(100))


# =========================
# TABLA: RESERVATIONS
# =========================
class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    destination = Column(String(100))
    people = Column(Integer)
    date = Column(Date)