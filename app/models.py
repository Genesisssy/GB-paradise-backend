from sqlalchemy import Column, Integer, String, Float, Date, Text, DECIMAL
from app.database import Base


class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    image = Column(String(255))
    price = Column(DECIMAL(10,2))
    old_price = Column(DECIMAL(10,2))
    rating = Column(Float)
    duration = Column(String(100))


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))
    destination = Column(String(100))
    people = Column(Integer)
    date = Column(Date)