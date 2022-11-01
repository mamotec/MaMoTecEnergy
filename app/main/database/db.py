"""
File for implementing connection to database
"""
from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:MaMoTec00001@localhost/mamotecenergy"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()


@lru_cache()
def create_session() -> scoped_session:
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return session


# Dependency
def get_session() -> Generator[scoped_session, None, None]:
    session = create_session()
    try:
        yield session
    finally:
        session.remove()
