#!/usr/bin/python
"""BaseModel module.

This module defines the BaseModel class, which defines all
common attributes/methods for other classes.
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """A base class for creating models with unique identifiers and timestamps.

    Public instance attributes:
    - id: str - A unique identifier generated using uuid.uuid4().
    - created_at: datetime - The datetime when the instance is created.
    - updated_at: datetime - The datetime when the instance is updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            timeformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, timeformat)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the object.

        formatted as:
        - "[ClassName] (id) {'attribute1': value1, 'attribute2': value2, ...}".
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime.

        This method updates the 'updated_at' attribute of the instance with the
        current datetime when it is called. It is typically used to indicate
        that the object has been modified or updated.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance.

        This method converts the instance into a dictionary representation:
        - The keys are the instance attributes (excluding private and special
          attributes).
        - The values are the corresponding values of the instance attributes.
        - An additional key '__class__' is added with the class name of the
          object.
        - The 'created_at' and 'updated_at' attributes are converted to ISO
          format strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
