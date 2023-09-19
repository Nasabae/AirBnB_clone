#!/usr/bin/python3
""" Class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
        Defines all common attributes/methods for other classes

        Attributes:
                   id: string - assigned with an uuid when
                                an instance is created
                   created_at: datetime of the instance created
                   updated_at: datetime is updated every
                               time you change your object
    """

    def __init__(self, *args, **kwargs):
        """
            Initializes objects
        """
        if (len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """
            Returns a string representation of the class BaseModel
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
            Returns a string representation of class BaseModel
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
             returns a dictionary containing all keys/values
             of __dict__ of the instance
        """
        cpy_d = dict(self.__dict__)
        cpy_d['__class__'] = self.__class__.__name__
        cpy_d['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        cpy_d['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return (cpy_d)
