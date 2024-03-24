#!/usr/bin/python3
"""Unit tests for the User class.

This module contains unit tests for the User class.
"""

import os
import unittest
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    @classmethod
    def setUp(self):
        """Set up method for the class"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tmp.json")

        self.obj = Place()

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
        self.assertEqual(str(type(self.obj)), "<class 'models.place.Place'>")

    def test_for_attributes(self):
        """Test if class attributes exists."""
        self.assertIn('name', dir(self.obj))
        self.assertNotIn('name', self.obj.__dict__)
        self.assertTrue(hasattr(self.obj, 'city_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'description'))
        self.assertTrue(hasattr(self.obj, 'number_of_rooms'))
        self.assertTrue(hasattr(self.obj, 'number_bathrooms'))
        self.assertTrue(hasattr(self.obj, 'max_guest'))
        self.assertTrue(hasattr(self.obj, 'price_by_night'))
        self.assertTrue(hasattr(self.obj, 'latitude'))
        self.assertTrue(hasattr(self.obj, 'longitude'))
        self.assertTrue(hasattr(self.obj, 'amenity_ids'))

    def test_for_attr_types(self):
        """Test for attribute types"""
        self.assertIsInstance(self.obj.city_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(self.obj.description, str)
        self.assertIsInstance(self.obj.number_of_rooms, int)
        self.assertIsInstance(self.obj.number_bathrooms, int)
        self.assertIsInstance(self.obj.max_guest, int)
        self.assertIsInstance(self.obj.price_by_night, int)
        self.assertIsInstance(self.obj.latitude, float)
        self.assertIsInstance(self.obj.longitude, float)
        self.assertIsInstance(self.obj.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
