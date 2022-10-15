"""
This module handles User information
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Implementation for user data and methods.

    Inherits from BaseModel with additional attributes.
    """

    email = str()
    """(str): User email address"""

    password = str()
    """(str): User password"""

    first_name = str()
    """(str): User first name"""

    last_name = str()
    """(str): User last name"""
