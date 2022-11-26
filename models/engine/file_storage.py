#!/usr/bin/python3

"""
Defines a class for File storage.
"""
import json
import os

class FileStorage():
    """
    Serializes instances to a JSON file and deserializes JSON
    file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return (self.__objects)

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        (path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists.

        Otherwise, do nothing.
        """
        if os.path.exists(self.__file_path):
            self.__objects = json.load(self.__file_path)
        else:
            pass
