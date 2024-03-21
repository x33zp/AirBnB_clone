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
        """Set up method for the class"""
        self.obj = User()
        self.obj_2 = User()
        self.obj.email = "zubbypeculiar@gmail.com"
        self.obj.password = "root"
        self.obj_dict = self.obj.to_dict()

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
        self.assertIsNotNone(self.obj.id)
        self.assertIsNotNone(self.obj.created_at)
        self.assertIsNotNone(self.obj.updated_at)
        self.assertTrue(issubclass(type(self.obj), BaseModel))

    def test_uuid(self):
        """Test uniqueness of UUID."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertNotEqual(self.obj.id, self.obj_2.id)
        self.assertIsInstance(self.obj.id, str)

    def test_datetime(self):
        """Test datetime attributes."""
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertNotEqual(self.obj.created_at,
                            self.obj_2.created_at)

    def test_for_attributes(self):
        """Test if class attributes exists."""
        self.assertIn('email', dir(self.obj_2))
        self.assertIsInstance(self.obj.email, str)
        self.assertTrue(hasattr(self.obj, 'email'))
        self.assertTrue(hasattr(self.obj, 'password'))
        self.assertTrue(hasattr(self.obj, 'first_name'))
        self.assertTrue(hasattr(self.obj, 'last_name'))
        self.assertNotIn('password', self.obj_2.__dict__)

    def test_init_with_attribute(self):
        """Test initialization with additional attribute."""
        self.obj.first_name = "Zubby"
        self.obj.last_name = "Peculiar"
        self.assertEqual(self.obj.first_name, "Zubby")
        self.assertIsInstance(self.obj.last_name, str)

    def test_str_representation(self):
        """Test string representation."""
        self.obj.name = "test_str"
        expected_str = "[User] ({}) {}".format(self.obj.id,
                                               self.obj.__dict__)
        self.assertEqual(str(self.obj), expected_str)

    def test_dict_representation(self):
        """Test dictionary representation."""
        created_iso = self.obj.created_at.isoformat()
        updated_iso = self.obj.updated_at.isoformat()
        self.assertEqual(self.obj_dict['id'], self.obj.id)
        self.assertEqual(self.obj_dict['__class__'], 'User')
        self.assertEqual(self.obj_dict['email'], 'zubbypeculiar@gmail.com')
        self.assertEqual(self.obj_dict['password'], 'root')
        self.assertEqual(self.obj_dict['created_at'], created_iso)
        self.assertEqual(self.obj_dict['updated_at'], updated_iso)

    def test_save(self):
        """Test save method."""
        self.obj.save()
        obj_dict_2 = self.obj.to_dict()
        self.assertNotEqual(self.obj_dict['updated_at'],
                            obj_dict_2['updated_at'])
        self.assertEqual(self.obj_dict['created_at'],
                         obj_dict_2['created_at'])

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs_model = User(**self.obj_dict)
        self.assertIsInstance(kwargs_model.id, str)
        self.assertEqual(kwargs_model.email, "zubbypeculiar@gmail.com")
        self.assertIsInstance(kwargs_model.created_at, datetime)
        self.assertIsNotNone(kwargs_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
