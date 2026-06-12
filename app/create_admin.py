from app.database import SessionLocal
from app.models import Admin


db = SessionLocal()

existing = db.query(Admin).filter(
    Admin.username == "admin"
).first()

if existing:

    print("⚠️ Admin ya existe")

else:

    admin = Admin(
        username="admin",
        password="gbparadise2026"
    )

    db.add(admin)

    db.commit()

    print("✅ Admin creado")