#!/usr/bin/python3
"""Module for BaseModel class."""
import models
from datetime import datetime
import uuid


class BaseModel:
    """Defines the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        t_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, j in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(j, t_form)
                else:
                    self.__dict__[k] = j
        else:
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance."""
        cliname = self.__class__.__name__
        return "[{}] ({}) {}".format(cliname, self.id, self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        frdict = self.__dict__.copy()
        frdict["created_at"] = self.created_at.isoformat()
        frdict["updated_at"] = self.updated_at.isoformat()
        frdict["__class__"] = self.__class__.__name__
        return frdict

