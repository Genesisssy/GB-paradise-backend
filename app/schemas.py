from pydantic import BaseModel
from datetime import date, datetime


# ======================
# OFFERS
# ======================
class OfferSchema(BaseModel):

    id: int

    title: str
    description: str
    image: str

    price: float
    old_price: float

    rating: float

    duration: str

    destination: str

    is_active: bool

    start_date: datetime
    end_date: datetime

    discount: str

    class Config:
        from_attributes = True


class OfferCreate(BaseModel):

    title: str
    description: str
    image: str

    price: float
    old_price: float

    rating: float

    duration: str

    destination: str

    start_date: datetime
    end_date: datetime

    discount: str


# ======================
# RESERVATIONS
# ======================
class ReservationSchema(BaseModel):

    full_name: str
    email: str
    phone: str

    destination: str

    people: int

    date: date


# ======================
# ADMIN
# ======================

class AdminLogin(BaseModel):

    username: str
    password: str