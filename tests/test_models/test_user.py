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

    def setUp(self):
        """Set up method for the class
        """
        self.user_model = User()
        self.user_model_2 = User()
        self.user_model.email = "zubbypeculiar@gmail.com"
        self.user_model.password = "root"
        self.model_dict = self.user_model.to_dict()

        if os.path.isfile("file.json"):
            os.rename("file.json", "tmp.json")

    def tearDown(self):
        """Tear down method for the class."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        elif os.path.isfile("tmp.json"):
            os.rename("tmp.json", "file.json")

    def test_init(self):
        """Test initialization of BaseModel."""
        self.assertIsNotNone(self.user_model.id)
        self.assertIsNotNone(self.user_model.created_at)
        self.assertIsNotNone(self.user_model.updated_at)
        self.assertTrue(issubclass(type(self.user_model), BaseModel))

    def test_uuid(self):
        """Test uniqueness of UUID."""
        self.assertTrue(hasattr(self.user_model, 'id'))
        self.assertNotEqual(self.user_model.id, self.user_model_2.id)
        self.assertIsInstance(self.user_model.id, str)

    def test_datetime(self):
        """Test datetime attributes."""
        self.assertTrue(hasattr(self.user_model, 'created_at'))
        self.assertTrue(hasattr(self.user_model, 'updated_at'))
        self.assertIsInstance(self.user_model.created_at, datetime)
        self.assertIsInstance(self.user_model.updated_at, datetime)
        self.assertNotEqual(self.user_model.created_at,
                         self.user_model_2.created_at)

    def test_for_attributes(self):
        """Test if class attributes exists."""
        self.assertIsInstance(self.user_model.email, str)
        self.assertTrue(hasattr(self.user_model, 'email'))
        self.assertTrue(hasattr(self.user_model, 'password'))
        self.assertTrue(hasattr(self.user_model, 'first_name'))
        self.assertTrue(hasattr(self.user_model, 'last_name'))

    def test_init_with_attribute(self):
        """Test initialization with additional attribute."""
        self.user_model.first_name = "Zubby"
        self.user_model.last_name = "Peculiar"
        self.assertEqual(self.user_model.first_name, "Zubby")
        self.assertIsInstance(self.user_model.last_name, str)

    def test_str_representation(self):
        """Test string representation."""
        self.user_model.name = "test_str"
        expected_str = "[User] ({}) {}".format(self.user_model.id,
                                               self.user_model.__dict__)
        self.assertEqual(str(self.user_model), expected_str)

    def test_dict_representation(self):
        """Test dictionary representation."""
        created_iso = self.user_model.created_at.isoformat()
        updated_iso = self.user_model.updated_at.isoformat()
        self.assertEqual(self.model_dict['id'], self.user_model.id)
        self.assertEqual(self.model_dict['__class__'], 'User')
        self.assertEqual(self.model_dict['email'], 'zubbypeculiar@gmail.com')
        self.assertEqual(self.model_dict['password'], 'root')
        self.assertEqual(self.model_dict['created_at'], created_iso)
        self.assertEqual(self.model_dict['updated_at'], updated_iso)

    def test_save(self):
        """Test save method."""
        self.user_model.save()
        model_dict_2 = self.user_model.to_dict()
        self.assertNotEqual(self.model_dict['updated_at'],
                            model_dict_2['updated_at'])

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs_model = User(**self.model_dict)
        self.assertIsInstance(kwargs_model.id, str)
        self.assertEqual(kwargs_model.email, "zubbypeculiar@gmail.com")
        self.assertIsInstance(kwargs_model.created_at, datetime)
        self.assertIsNotNone(kwargs_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
