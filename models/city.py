#!/usr/bin/python3
"""City module.

This module which inherits from BaseModel defines the City
class, which represents the City of each user of the
application.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class represents a City."""
    state_id = ""
    name = ""