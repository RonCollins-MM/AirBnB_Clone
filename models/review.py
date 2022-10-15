"""
This module handles the Review class
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Implementation of Review class
    """

    place_id = str()
    """
    (str): Will be Place.id
    """
    user_id = str()
    """
    (str): Will be User.id
    """
    text = str()
    """
    (str): The actual review
    """
