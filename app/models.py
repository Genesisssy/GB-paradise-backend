from sqlalchemy import Column, Integer, String, Float, Date, Boolean, DateTime
from app.database import Base


# ======================
# OFFERS TABLE
# ======================
class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255))
    description = Column(String(500))
    destination = Column(String(255))

    image = Column(String(255))

    price = Column(Float)
    old_price = Column(Float)

    discount = Column(String(20))

    rating = Column(Float)

    duration = Column(String(50))

    is_active = Column(Boolean, default=True)

    start_date = Column(DateTime)

    end_date = Column(DateTime)

# ======================
# RESERVATIONS TABLE
# ======================
class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(50))

    destination = Column(String(255))

    people = Column(Integer)

    date = Column(Date)


# ======================
# ADMINS TABLE
# ======================
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(255), unique=True)

    password = Column(String(255))