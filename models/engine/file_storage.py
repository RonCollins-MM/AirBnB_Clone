"""
This module contains implementation for FileStorage class that is responsible
to storage of objects to files and reading objects from files.
"""

from models.base_model import BaseModel
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
        Sets in __objects the passed object with key as ``<class name>.id`` and
        value as instance object of its respective class.

        Args:
            obj: The object to be stored
        """

        self.__objects.update({f'{obj.__class__.__name__}.{obj.id}' : \
                          obj})

    def save(self):
        """
        Serializes __objects to JSON file at the path specified in __file_path
        attribute.

        A local copy of ``__objects`` is created and then each object is converted
        to its dictionary representation before being dumped into the JSON file.
        """

        lcl_copy = self.__objects
        obj_as_dict = {key: lcl_copy[key].to_dict() for key in lcl_copy.keys()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(obj_as_dict))

    def reload(self):
        """
        Deserializes JSON file to ``__objects``.

        All dictionary representation of objects are first converted to objects
        instances of their respective classes before being added to the
        ``__objects`` attribute.
        If the file doesn't exist, nothing happens.
        """

        if os.path.exists(self.__file_path):
            with open (self.__file_path, 'r', encoding='utf-8') as f:
                obj_as_dict = json.loads(f.read())
                for v in obj_as_dict.values():
                    #Class name is obtained from the dictionary then
                    #class constructor called to create an object.
                    #The object is then passed to self.new() to append object
                    #to __objects attribute
                    self.new(eval(v['__class__'])(**v))
