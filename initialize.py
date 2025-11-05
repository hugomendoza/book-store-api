from app.db.connection.database import engine
from app.db.models.models import Base

def init_db():
    print("Initializing database...")
    Base.metadata.create_all(engine)
    print("Database initialized successfully.")

init_db()