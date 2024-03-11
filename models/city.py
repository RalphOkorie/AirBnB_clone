#!/usr/bin/python3
"""Defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city class that inherits from BaseModel class"""
    state_id = ""
    name = ""
