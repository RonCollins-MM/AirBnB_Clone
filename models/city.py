"""
This module handles the City class
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    Implementation of City class
    """

    name = str()
    """
    (str): Name of a City
    """

    state_id = str()
    """
    (str): Will contain the id of the State it is found
    """
