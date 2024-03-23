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
        self.obj_2 = Place()
        self.obj.city_id = "12345"
        self.obj.max_guest = 2
        self.obj.amenity_ids = ["1234", "5678"]
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
        self.assertIn('name', dir(self.obj))
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
        self.assertNotIn('name', self.obj.__dict__)

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

    def test_init_with_attribute(self):
        """Test initialization with additional attribute."""
        self.obj.name = "Santorini Hotel"
        self.assertEqual(self.obj.name, "Santorini Hotel")
        self.assertIn('name', self.obj.__dict__)

    def test_str_representation(self):
        """Test string representation."""
        self.obj.name = "test_str"
        expected_str = "[Place] ({}) {}".format(self.obj.id,
                                                self.obj.__dict__)
        self.assertEqual(str(self.obj), expected_str)

    def test_dict_representation(self):
        """Test dictionary representation."""
        created_iso = self.obj.created_at.isoformat()
        updated_iso = self.obj.updated_at.isoformat()
        self.assertEqual(self.obj_dict['id'], self.obj.id)
        self.assertEqual(self.obj_dict['__class__'], "Place")
        self.assertEqual(self.obj_dict['city_id'], "12345")
        self.assertEqual(self.obj_dict['max_guest'], 2)
        self.assertEqual(self.obj_dict['amenity_ids'], ["1234", "5678"])
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
        kwargs_model = Place(**self.obj_dict)
        self.assertIsInstance(kwargs_model.id, str)
        self.assertIsInstance(kwargs_model.max_guest, int)
        self.assertIsInstance(kwargs_model.amenity_ids, list)
        self.assertEqual(kwargs_model.city_id, "12345")
        self.assertIsInstance(kwargs_model.created_at, datetime)
        self.assertIsNotNone(kwargs_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
