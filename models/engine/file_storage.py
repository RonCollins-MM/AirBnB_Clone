"""
This module contains implementation for FileStorage class that is responsible
to storage of objects to files and reading objects from files.
"""

import json
import os

class FileStorage():
    """
    Handles serialization of instances to JSON files and deserialization of
    JSON files to instances.

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (:obj: `dict`): Initially empty but will store all objects by
        ``<class name>.id`` Example. ``BaseModel`` object with ``id=112233``, the key will
        be ``BaseModel.112233``
    """

    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """
        Will return the private attribute __objects that contains all objects
        to be stored.
        """

        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the passed object with the key <class name>.id. It is
        the responsibility of the caller of this method to pass an object as a
        dictionary representation.

        Args:
            obj (:obj: `dict`): The object to be stored
        """

        __objects.update({f'{obj.__class__.__name__}.{obj.id}' : \
                          '{obj}'})

    def save(self):
        """
        Serializes __objects to JSON file at the path specified in __file_path
        attribute
        """

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """
        Deserializes JSON file to ``__objects``. If the file doesn't exist,
        nothing happens.
        """

        if os.path.exists(self.__file_path):
            with open (__file_path, 'r', encoding='utf-8') as f:
                self.__objects = json.loads(f.read())
