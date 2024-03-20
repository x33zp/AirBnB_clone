#!/usr/bin/python3
"""Unit tests for the BaseModel class.

This module contains unit tests for the BaseModel class.
"""

import os
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """setUp method for the class"""
        self.base_model = BaseModel()
        self.base_model_2 = BaseModel()
        self.base_model.name = "TestBaseModel"
        self.base_model.number = 89
        self.model_dict = self.base_model.to_dict()

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
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsNotNone(self.base_model.id)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsNotNone(self.base_model.updated_at)

    def test_uuid(self):
        """Test uniqueness of UUID."""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertNotEqual(self.base_model.id, self.base_model_2.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_datetime(self):
        """Test datetime attributes."""
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_init_with_attribute(self):
        """Test initialization with additional attribute."""
        self.base_model.author = "zubby peculiar"
        self.assertEqual(self.base_model.author, "zubby peculiar")
        self.assertIsInstance(self.base_model.name, str)
        self.assertIsInstance(self.base_model.number, int)

    def test_str_representation(self):
        """Test string representation."""
        self.base_model.name = "test_str"
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id,
                                                    self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_dict_representation(self):
        """Test dictionary representation."""
        self.base_model.name = "test_dict"
        obj_dict = self.base_model.to_dict()
        created_iso = self.base_model.created_at.isoformat()
        updated_iso = self.base_model.updated_at.isoformat()
        self.assertEqual(obj_dict['id'], self.base_model.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['name'], 'test_dict')
        self.assertEqual(obj_dict['number'], 89)
        self.assertEqual(obj_dict['created_at'], created_iso)
        self.assertEqual(obj_dict['updated_at'], updated_iso)

    def test_save(self):
        """Test save method."""
        self.base_model.name = "test_save"
        self.base_model.save()
        model_dict_2 = self.base_model.to_dict()
        self.assertNotEqual(self.model_dict['updated_at'],
                            model_dict_2['updated_at'])

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments."""
        kwargs_model = BaseModel(**self.model_dict)
        self.assertEqual(kwargs_model.name, "TestBaseModel")
        self.assertEqual(kwargs_model.number, 89)
        self.assertIsInstance(kwargs_model.created_at, datetime)


if __name__ == '__main__':
    unittest.main()
