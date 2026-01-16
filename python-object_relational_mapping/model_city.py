#!/usr/bin/python3
"""
City model module for SQLAlchemy ORM.
Defines the City class with foreign key to states table.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class representing the cities table.

    Attributes:
        id: Primary key, auto-incremented integer
        name: City name, string up to 128 characters
        state_id: Foreign key referencing states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
