from app.database import SessionLocal
from app.models import Admin


def seed_admin():

    db = SessionLocal()

    try:

        existing = db.query(Admin).filter(
            Admin.username == "admin"
        ).first()

        if existing:

            print("⚠️ Admin ya existe")

            return

        admin = Admin(
            username="admin",
            password="gbparadise2026"
        )

        db.add(admin)

        db.commit()

        print("✅ Admin creado correctamente")

    finally:

        db.close()


if __name__ == "__main__":
    seed_admin()