#!/usr/bin/python3
"""Amenity module.

This module which inherits from BaseModel defines the
Amenity class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class represents Amenity."""
    name = ""