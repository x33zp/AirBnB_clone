#!/usr/bin/python3
"""Unit tests for the User class.

This module contains unit tests for the User class.
"""

import os
import unittest
from models.state import State
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up method for the class"""
        self.state_model = State()
        self.state_model_2 = State()
        self.state_model.name = "Rivers"
        self.model_dict = self.state_model.to_dict()

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
        self.assertIsNotNone(self.state_model.id)
        self.assertIsNotNone(self.state_model.created_at)
        self.assertIsNotNone(self.state_model.updated_at)
        self.assertTrue(issubclass(type(self.state_model), BaseModel))

    def test_uuid(self):
        """Test uniqueness of UUID."""
        self.assertTrue(hasattr(self.state_model, 'id'))
        self.assertNotEqual(self.state_model.id, self.state_model_2.id)
        self.assertIsInstance(self.state_model.id, str)

    def test_datetime(self):
        """Test datetime attributes."""
        self.assertTrue(hasattr(self.state_model, 'created_at'))
        self.assertTrue(hasattr(self.state_model, 'updated_at'))
        self.assertIsInstance(self.state_model.created_at, datetime)
        self.assertIsInstance(self.state_model.updated_at, datetime)
        self.assertNotEqual(self.state_model.created_at,
                            self.state_model_2.created_at)

    def test_for_attributes(self):
        """Test if class attributes exists."""
        self.assertIn('name', dir(self.state_model_2))
        self.assertTrue(hasattr(self.state_model, 'name'))
        self.assertIsInstance(self.state_model.name, str)
        self.assertNotIn('name', self.state_model_2.__dict__)

    def test_init_with_attribute(self):
        """Test initialization with additional attribute."""
        self.state_model.name = "Lagos"
        self.assertEqual(self.state_model.name, "Lagos")
        self.assertIsInstance(self.state_model.name, str)

    def test_str_representation(self):
        """Test string representation."""
        self.state_model.name = "test_str"
        expected_str = "[State] ({}) {}".format(self.state_model.id,
                                                self.state_model.__dict__)
        self.assertEqual(str(self.state_model), expected_str)

    def test_dict_representation(self):
        """Test dictionary representation."""
        created_iso = self.state_model.created_at.isoformat()
        updated_iso = self.state_model.updated_at.isoformat()
        self.assertEqual(self.model_dict['id'], self.state_model.id)
        self.assertEqual(self.model_dict['__class__'], 'State')
        self.assertEqual(self.model_dict['name'], 'Rivers')
        self.assertEqual(self.model_dict['created_at'], created_iso)
        self.assertEqual(self.model_dict['updated_at'], updated_iso)

    def test_save(self):
        """Test save method."""
        self.state_model.save()
        model_dict_2 = self.state_model.to_dict()
        self.assertNotEqual(self.model_dict['updated_at'],
                            model_dict_2['updated_at'])
        self.assertEqual(self.model_dict['created_at'],
                         model_dict_2['created_at'])

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs_model = State(**self.model_dict)
        self.assertIsInstance(kwargs_model.id, str)
        self.assertEqual(kwargs_model.name, "Rivers")
        self.assertIsInstance(kwargs_model.created_at, datetime)
        self.assertIsNotNone(kwargs_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
