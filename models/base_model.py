#!/usr/bin/python3

"""The BaseModel class."""
import uuid
import datetime
from models import storage

class BaseModel():
    """
    Defines all common attributes/methods for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiates an object of the class.
        Attributes:
                id: a unique instance id.
                created_at: datetime when instance was created.
                updated_at: datetime when instance was updated
                    initially set to created_at.
                __class__: skip this attribute if given.
        """
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    format = "%Y-%m-%dT%H:%M:%S.%f"
                    v = datetime.datetime.strptime(v, format)
                if k == "__class__":
                    continue
                setattr(self, k, v)

        attr = {
                "id": str(uuid.uuid4()),
                "created_at": datetime.datetime.now(),
                "updated_at": datetime.datetime.now()
                }
        [setattr(self, key, val) for key, val in attr.items()
                if not hasattr(self, key)]
        if kwargs is None:
            storage.save()

    def __str__(self):
        """
        Defines an output for the instance on print() on all:
            [<class name>] (<self.id>) <self.__dict__>
        """
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__)
        return string

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of
        __dict__ of the instance adding a __class__ key to the
        dictionary.
        """
        dicti = self.__dict__
        dicti["__class__"] = self.__class__.__name__
        dicti["updated_at"] = self.updated_at.isoformat()
        dicti["created_at"] = self.created_at.isoformat()
        return dicti
