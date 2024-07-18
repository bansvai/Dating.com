from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Path to the database file
DATABASE_URL = "sqlite:///./dating.db"

# SQLite engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Sessionmaker for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models that includes ORM features
Base = declarative_base()