from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import setting
# from database.base import Base
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{setting.POSTGRES_USER}:{setting.POSTGRES_PASSWORD}@{setting.POSTGRES_HOSTNAME}:{setting.POSTGRES_PORT}/{setting.POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
