#!/usr/bin/python3
"""Unit tests for the FileStorage class.

This module contains unit tests for the FileStorage class.
"""

import os
import json
import unittest
from models import storage
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    @classmethod
    def setUp(self):
        """Set up method for the class"""
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.rename(FileStorage._FileStorage__file_path, 'tmp.json')

        self.all_objs = storage.all()
        self.classes = {'BaseModel', 'User', 'State', 'City', 'Amenity',
                        'Place', 'Review'}

    @classmethod
    def tearDown(self):
        """Tear down method for the class."""
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        if os.path.isfile("tmp.json"):
            os.rename("tmp.json", FileStorage._FileStorage__file_path)
        FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """Test for instance creation."""
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_for_private_attr(self):
        """Test for existence of private attributes."""
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))

    def test_for_attr_types(self):
        """Test for correct attribute types."""
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_all(self):
        """Test for the 'all' method."""
        for obj in self.classes:
            eval(obj)()
        self.assertIsNotNone(self.all_objs)
        for obj_id in FileStorage._FileStorage__objects:
            obj = FileStorage._FileStorage__objects[obj_id]
            obj_dict = obj.to_dict()
            self.assertIn(obj_dict['__class__'], self.classes)

    def test_new(self):
        """Test for the 'new' method."""
        for obj in self.classes:
            model_obj = eval(obj)()
            storage.new(model_obj)
            key = "{}.{}".format(type(model_obj).__name__, model_obj.id)
            self.assertIn(key, FileStorage._FileStorage__objects)

    def test_save(self):
        """Test for the 'save' method."""
        # os.remove(FileStorage.FileStrorage__file_path)
        # FileStorage._FileStorage__objects = {}
        self.assertEqual(self.all_objs, {})
        self.assertFalse(os.path.isfile(FileStorage._FileStorage__file_path))
        for obj in self.classes:
            model_obj = eval(obj)()
            storage.new(model_obj)
            storage.save()
            key = "{}.{}".format(type(model_obj).__name__, model_obj.id)
            with open(FileStorage._FileStorage__file_path, 'r') as jsonfile:
                text = jsonfile.read()
                self.assertIn(key, text)
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test for the 'reload' method."""
        for obj in self.classes:
            model_obj = eval(obj)()
            storage.new(model_obj)
            storage.save()
            storage.reload()
            key = "{}.{}".format(type(model_obj).__name__, model_obj.id)
            self.assertIn(key, FileStorage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
