#!/usr/bin/python3
"""Unit tests for the User class.

This module contains unit tests for the User class.
"""

import os
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    @classmethod
    def setUp(self):
        """Set up method for the class"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tmp.json")

        self.obj = Amenity()

    @classmethod
    def tearDown(self):
        """Tear down method for the class."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("tmp.json"):
            os.rename("tmp.json", "file.json")

    def test_init(self):
        """Test initialization of BaseModel."""
        self.assertTrue(issubclass(type(self.obj), BaseModel))
        self.assertEqual(str(type(self.obj)),
                         "<class 'models.amenity.Amenity'>")

    def test_for_attributes(self):
        """Test if class attributes exists."""
        self.assertIn('name', dir(self.obj))
        self.assertTrue(hasattr(self.obj, 'name'))
        self.assertIsInstance(self.obj.name, str)
        self.assertNotIn('name', self.obj.__dict__)


if __name__ == '__main__':
    unittest.main()
