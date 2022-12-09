from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config.database import settings

engine = settings.postgres_uri

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(
        engine,
        isolation_level="REPEATABLE READ",
        # connect_args={"check_same_thread": False}, # only sqlite. allow multiple acces to database, Each request has its own session
    ),
)

Base = declarative_base()