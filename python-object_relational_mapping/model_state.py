#!/usr/bin/python3
"""
State model module for SQLAlchemy ORM.
Defines the State class mapped to the states table.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class representing the states table.

    Attributes:
        id: Primary key, auto-incremented integer
        name: State name, string up to 128 characters
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
