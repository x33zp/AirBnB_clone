#!/usr/bin/python3
import os
import unittest
from models import storage
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up method for the class"""
        if os.path.isfile(storage._FileStorage__file_path):
            os.rename(storage._FileStorage__file_path, 'tmp.json')

        storage._FileStorage__objects = {}
        self.all_objs = storage.all()
        self.classes = {'BaseModel', 'User', 'State', 'City', 'Amenity',
                        'Place', 'Review'}

    def tearDown(self):
        """Tear down method for the class."""
        if os.path.isfile(storage._FileStorage__file_path):
            os.remove(storage._FileStorage__file_path)
        if os.path.isfile("tmp.json"):
            os.rename("tmp.json", storage._FileStorage__file_path)