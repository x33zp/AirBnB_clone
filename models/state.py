#!/usr/bin/python3
"""State module.

This module which inherits from BaseModel defines the State
class, which represents the state of each user of the
application.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """This class represents a State."""
    name = ""