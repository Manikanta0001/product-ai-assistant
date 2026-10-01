"""Database foundation using SQLAlchemy 2.x.

Reads DATABASE_URL from environment variables.
Does not create tables (no Base.metadata.create_all here).
"""

import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "")


class Base(DeclarativeBase):
    pass


# Only create engine/session factory when DATABASE_URL is configured.
# This keeps `import database` safe for tests that do not need PostgreSQL.
engine = create_engine(DATABASE_URL) if DATABASE_URL else None

SessionLocal = (
    sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
    if engine is not None
    else None
)


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency that provides a database session."""
    if SessionLocal is None:
        raise RuntimeError("DATABASE_URL is not set. Configure it in your environment.")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
