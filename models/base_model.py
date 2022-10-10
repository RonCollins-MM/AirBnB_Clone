"""
BaseClass Module - Contains the implementation for the Base Class superclass.
"""

import datetime
import uuid

class BaseModel():
    """
    Implementation for the BaseModel class.

    Defines all common attributes and methods for child classes.
    """

    def __init__(self):
        """
        Constructor for BaseModel class.

        Does intialisation of public attributes as described below
        """

        self.id = str(uuid.uuid4())
        """str - Unique identifier for each instance"""

        self.created_at = datetime.datetime.now()
        """datetime: Time when instance is created """

        self.updated_at = self.created_at
        """datetime: Time stamp when instance attributes were last modified.

        Is first initialized to when instance was created and is updated with
        every modification.
        """

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
        """Returns string representation of the instance.

        Format:
            [<Class name>] (<self.id>) <self.__dict__>
        """

    def save(self):
        self.updated_at = datetime.datetime.now()
        """
        Updates the time stamp for when instance attributes are modified with
        current datetime.
        """

    def to_dict(self):
        inst_dict = dict(self.__dict__)
        inst_dict.update({'__class__': f'{self.__class__.__name__}'})
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()

        return inst_dict
        """
        Generates a dictionary object of the current instance.

        A key '__class__' is added with the class name of the object. The
        values for the ``created_at`` and ``updated_at`` attributes are
        converted to ISO datetime format.

        Returns:
            Dictionary object of the created instance of class.

        """
