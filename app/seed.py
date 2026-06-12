import json
from datetime import datetime

from app.database import SessionLocal
from app.models import Offer


# ======================
# CARGAR JSON → MYSQL
# ======================
def seed_offers():

    db = SessionLocal()

    try:

        # Cargar JSON
        with open(
            "data/offers.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        # Evitar duplicados
        existing = db.query(Offer).first()

        if existing:

            print(
                "⚠️ Ya hay datos en offers, seed cancelado"
            )

            return

        # Insertar ofertas
        for item in data:

            offer = Offer(

                title=item["title"],
                description=item["description"],
                destination=item["destination"],

                image=item["image"],

                price=item["price"],
                old_price=item["old_price"],

                discount=item["discount"],

                rating=item["rating"],

                duration=item["duration"],

                is_active=item["is_active"],

                start_date=datetime.fromisoformat(
                    item["start_date"]
                ),

                end_date=datetime.fromisoformat(
                    item["end_date"]
                ),
            )

            db.add(offer)

        db.commit()

        print(
            f"🔥 {len(data)} ofertas cargadas correctamente"
        )

    except Exception as e:

        db.rollback()

        print(
            f"❌ Error cargando ofertas: {e}"
        )

    finally:

        db.close()


# ======================
# EJECUTAR SEED
# ======================
if __name__ == "__main__":

    seed_offers()