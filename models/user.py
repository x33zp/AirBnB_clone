#!/usr/bin/python
"""User module.

This module which inherits from BaseModel defines the User
class, which represents a user of the application.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a user."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""