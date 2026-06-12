from pydantic import BaseModel
from datetime import date


class OfferSchema(BaseModel):
    id: int
    title: str
    description: str
    image: str
    price: float
    old_price: float
    rating: float
    duration: str

    class Config:
        from_attributes = True


class ReservationSchema(BaseModel):
    full_name: str
    email: str
    phone: str
    destination: str
    people: int
    date: date