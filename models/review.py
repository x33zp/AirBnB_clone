#!/usr/bin/python3
"""Review module.

This module which inherits from BaseModel defines the State
class, which represents the reviews given by the User.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class represents Review."""

    place_id = ""
    user_id = ""
    text = ""
