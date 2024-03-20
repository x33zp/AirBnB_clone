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
        """_summary_
        """
        base_model = BaseModel()
        base_model.name = "TestBaseModel"
        base_model.number = 1
        self.assertTrue(hasattr(base_model, 'name'))
        self.assertIsInstance(base_model.name, str)
        self.assertIsInstance(base_model.number, int)

    def test_str_representation(self):
        """_summary_
        """
        base_model = BaseModel()
        base_model.name = "TestBaseModel"
        base_model.number = 2
        expected_str = "[BaseModel] ({}) {}".format(base_model.id,
                                                    base_model.__dict__)
        self.assertEqual(str(base_model), expected_str)

    def test_dict_representation(self):
        """_summary_
        """
        base_model = BaseModel()
        base_model.name = "TestBaseModel"
        base_model.number = 3
        obj_dict = base_model.to_dict()
        created_iso = base_model.created_at.isoformat()
        updated_iso = base_model.updated_at.isoformat()
        self.assertEqual(obj_dict['id'], base_model.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['name'], 'TestBaseModel')
        self.assertEqual(obj_dict['number'], 3)
        self.assertEqual(obj_dict['created_at'], created_iso)
        self.assertEqual(obj_dict['updated_at'], updated_iso)

    def test_save(self):
        """_summary_
        """
        base_model = BaseModel()
        pass

    def test_kwargs(self):
        """_summary_
        """
        base_model = BaseModel()
        base_model.name = "TestBaseModel"
        base_model.number = 5


if __name__ == '__main__':
    unittest.main()
