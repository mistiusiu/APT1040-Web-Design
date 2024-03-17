#!/usr/bin/python3
""" holds class Place"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """Representation of place """
    if models.storage_t == "db":
        __tablename__ = 'states'
        picture = Column(String(255), nullable=False)
        title = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)

    else:
        picture = ""
        title = ""
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)