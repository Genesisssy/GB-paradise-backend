from app.database import engine
from app.models import Base

print("🗑 Eliminando tablas...")

Base.metadata.drop_all(bind=engine)

print("✅ Tablas eliminadas")

print("🔨 Creando tablas nuevas...")

Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas")