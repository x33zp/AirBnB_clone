#!/usr/bin/python3
"""Unit tests for the User class.

This module contains unit tests for the User class.
"""

import os
import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    @classmethod
    def setUp(self):
        """Set up method for the class"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tmp.json")

        self.obj = User()

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
        self.assertEqual(str(type(self.obj)), "<class 'models.user.User'>")

    def test_for_attributes(self):
        """Test if class attributes exists."""
        self.assertIn('email', dir(self.obj))
        self.assertNotIn('password', self.obj.__dict__)
        self.assertIsInstance(self.obj.password, str)
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))

    def test_for_attributes(self):
        """Test if class attributes exists."""
        self.assertIsInstance(self.obj.email, str)
        self.assertIsInstance(self.obj.password, str)
        self.assertIsInstance(self.obj.first_name, str)
        self.assertIsInstance(self.obj.last_name, str)
        self.assertIsInstance(self.obj.password, str)


if __name__ == '__main__':
    unittest.main()
