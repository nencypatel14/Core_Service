from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import settings
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
