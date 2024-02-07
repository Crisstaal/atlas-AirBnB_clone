#!/usr/bin/python3
""" Module that implements the City class"""
from models.base_model import BaseModel

class City(BaseModel):
    """Class representing a city"""
    state_id = ""
    name = ""