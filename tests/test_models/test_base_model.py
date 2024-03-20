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
