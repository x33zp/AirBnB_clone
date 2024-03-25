#!/usr/bin/python3
"""Unit tests for the BaseModel class.

This module contains unit tests for the BaseModel class.
"""

import os
import unittest
from datetime import datetime
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    @classmethod
    def setUp(self):
        """setUp method for the class"""
        if os.path.isfile("file.json"):
            os.rename("file.json", "tmp.json")

        self.obj = BaseModel()
        self.obj_dict = self.obj.to_dict()


    @classmethod
    def tearDown(self):
        """Tear down method for the class."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        if os.path.isfile("tmp.json"):
            os.rename("tmp.json", "file.json")

    def test_init(self):
        """Test initialization of BaseModel."""
        self.assertIsInstance(self.obj, BaseModel)
        self.assertEqual(str(type(self.obj)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsNotNone(self.obj.id)
        self.assertIsNotNone(self.obj.created_at)
        self.assertIsNotNone(self.obj.updated_at)

    def test_uuid(self):
        """Test uniqueness of UUID."""
        self.assertTrue(hasattr(self.obj, 'id'))
        self.assertIsInstance(self.obj.id, str)

    def test_datetime(self):
        """Test datetime attributes."""
        self.assertTrue(hasattr(self.obj, 'created_at'))
        self.assertTrue(hasattr(self.obj, 'updated_at'))
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_init_with_attribute(self):
        """Test initialization with additional attribute."""
        self.obj.author = "zubby peculiar"
        self.assertEqual(self.obj.author, "zubby peculiar")

    def test_str_representation(self):
        """Test string representation."""
        self.obj.name = "test_str"
        expected_str = "[BaseModel] ({}) {}".format(self.obj.id,
                                                    self.obj.__dict__)
        self.assertEqual(str(self.obj), expected_str)

    def test_dict_representation(self):
        """Test dictionary representation."""
        self.obj.name = "test_dict"
        obj_dict = self.obj.to_dict()
        created_iso = self.obj.created_at.isoformat()
        updated_iso = self.obj.updated_at.isoformat()
        self.assertEqual(obj_dict['id'], self.obj.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], created_iso)
        self.assertEqual(obj_dict['updated_at'], updated_iso)

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
        kwargs_model = BaseModel(**self.obj_dict)
        self.assertEqual(kwargs_model.id, self.obj.id)
        self.assertIsInstance(kwargs_model.created_at, datetime)


if __name__ == '__main__':
    unittest.main()
