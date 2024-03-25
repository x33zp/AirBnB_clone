#!/usr/bin/python3
"""Unit tests for the User class.

This module contains unit tests for the User class.
"""

import os
import unittest
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    @classmethod
    def setUp(self):
        """Set up method for thr class"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tmp.json")

        self.obj = Review()

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
        self.assertEqual(str(type(self.obj)), "<class 'models.review.Review'>")

    def test_for_attributes(self):
        """Test if class attributes exists."""
        self.assertIn('user_id', dir(self.obj))
        self.assertNotIn('user_id', self.obj.__dict__)
        self.assertTrue(hasattr(self.obj, 'place_id'))
        self.assertTrue(hasattr(self.obj, 'user_id'))
        self.assertTrue(hasattr(self.obj, 'text'))

    def test_for_attr_types(self):
        """Test for attribute types"""
        self.assertIsInstance(self.obj.place_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.text, str)

if __name__ == '__main__':
    unittest.main()
