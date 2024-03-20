#!/usr/bin/python3
"""_summary_
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """_summary_
    """
    def test_init(self):
        """_summary_
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsNotNone(base_model.id)
        self.assertIsNotNone(base_model.created_at)
        self.assertIsNotNone(base_model.updated_at)

    def test_uuid(self):
        """_summary_
        """
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertTrue(hasattr(base_model_1, 'id'))
        self.assertNotEqual(base_model_1.id, base_model_2.id)
        self.assertIsInstance(base_model_1.id, str)

    def test_datetime(self):
        """_summary_
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_init_with_attribute(self):
        """_summary_
        """
        pass


if __name__ == '__main__':
    unittest.main()