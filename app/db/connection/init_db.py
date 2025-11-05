from .database import engine
from ..models.models import Base

def init_db():
    print("Initializing database...")
    Base.metadata.create_all(engine)