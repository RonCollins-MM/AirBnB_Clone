"""
This module handles the Place class
"""

from models.base_model import BaseModel

class Place(BaseModel):
    """
    Implementation of Place class
    """

    city_id = ''
    """
    (str): Will hold the id of the City it is found
    """

    user_id = ''
    """
    (str): Will hold the id of the State it is found
    """

    name = ''
    """
    (str): Name of a place
    """

    description = ''
    """
    (str): Will hold the description of the place
    """

    number_rooms = 0
    """
    (int): The number of rooms of the place
    """

    number_bathrooms = 0
    """
    (int): The number of bathrooms of the place
    """

    max_guest = 0
    """
    (int): The maximum guests the place can host
    """

    price_by_night = 0
    """
    (int): The price of lodging per night
    """

    latitude = 0.0
    """
    (float): Latitude of the place
    """

    longitude = 0.0
    """
    (float): Longitude of the place
    """

    amenity_ids = list()
    """
    (:obj :``list``): Will be list of Amenity.id later
    """
