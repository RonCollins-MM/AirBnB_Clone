"""
This module handles the City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Implementation of City class
    """

    name = ''
    """
    (str): Name of a City
    """

    state_id = ''
    """
    (str): Will contain the id of the State it is found
    """
