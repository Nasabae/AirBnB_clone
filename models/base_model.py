#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""
Base Model class
"""


class BaseModel:
    """
    Base class defining all attributes and methods
    """

    def __init__(self, *args, **kwargs):
        """Initializing the attributes"""
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    pass
                elif k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of the class name,
        id and dictionary
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the time whenever it's called"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns dictionary containing all dicts values instances"""
        my_dict = {}
        my_dict["__class__"] = self.__class__.__name__
        for attr in self.__dict__:
            if attr == "created_at" or attr == "updated_at":
                my_dict[attr] = getattr(self, attr).isoformat()
            else:
                my_dict[attr] = getattr(self, attr)
        return my_dict
