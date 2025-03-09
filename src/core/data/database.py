"""
Database setup and connection handling.
"""
from typing import Optional
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from config.settings import DATABASE_URI

# Create directory for database if it doesn't exist
db_path = Path(DATABASE_URI.split('///')[-1]).parent
os.makedirs(db_path, exist_ok=True)

# Create engine and session
engine = create_engine(DATABASE_URI, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()

def get_db() -> Session:
    """
    Get a database session.
    
    Returns:
        A SQLAlchemy Session instance
    """
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

def init_db() -> None:
    """
    Initialize the database, creating all tables.
    """
    # Import all models to ensure they're registered with Base
    from core.data.models import User
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
def reset_db() -> None:
    """
    Reset the database by dropping and recreating all tables.
    WARNING: This will delete all data!
    """
    Base.metadata.drop_all(bind=engine)
    init_db()