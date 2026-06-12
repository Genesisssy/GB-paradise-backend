import json
from app.database import SessionLocal
from app.models import Offer


# ======================
# CARGAR JSON → MYSQL
# ======================
def seed_offers():
    db = SessionLocal()

    try:
        # cargar JSON local
        with open("data/offers.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        # evitar duplicados
        existing = db.query(Offer).first()
        if existing:
            print("⚠️ Ya hay datos en offers, seed cancelado")
            return

        # insertar datos
        for item in data:
            offer = Offer(
                title=item["title"],
                description=item["description"],
                image=item["image"],
                price=item["price"],
                old_price=item["old_price"],
                rating=item["rating"],
                duration=item["duration"],
            )
            db.add(offer)

        db.commit()
        print("🔥 Offers cargadas correctamente")

    finally:
        db.close()