from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app.config.envs as envs

DB_USER = envs.POSTGRES_USER
DB_PASSWORD = envs.POSTGRES_PASSWORD
DB_HOST = envs.POSTGRES_HOST
DB_PORT = envs.POSTGRES_PORT
DB_NAME = envs.POSTGRES_DB

database_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(database_url, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()