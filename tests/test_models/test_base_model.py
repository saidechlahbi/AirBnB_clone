#!/usr/bin/python3
"""Test module for BaseModel class."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines the TestBaseModel class."""

    def test_attributes(self):
        """Test initialization of BaseModel attributes."""
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertNotEqual(base.id, base2.id)

    def test_str_representation(self):
        """Test the __str__ method of BaseModel."""
        my_model = BaseModel()
        str_representation = "[BaseModel] ({}) {}".format(my_model.id,
                                                          my_model.__dict__)
        self.assertEqual(str(my_model), str_representation)
        self.assertEqual(base.__str__(),
                         f"[{type(base).__name__}] \
({base.id}) {base.__dict__}")

    def test_save_method(self):
        """Test the save method of BaseModel."""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict)
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertIsInstance(my_model_json["created_at"], str)
        self.assertIsInstance(my_model_json["updated_at"], str)

    def test_from_dict_method(self):
        """Test the creation of BaseModel instance from dictionary."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)

    def test_save_reload(self):
        """Test the save and reload functionality."""
        all_objs_before = storage.all()

        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        storage.reload()
        all_objs_after = storage.all()

        self.assertGreater(len(all_objs_after), len(all_objs_before))

        keys_after = set(all_objs_after.keys())
        keys_before = set(all_objs_before.keys())

        self.assertTrue(keys_after.issuperset(keys_before))

        for key in keys_before:
            obj_after = all_objs_after[key]
            obj_before = all_objs_before[key]
            self.assertEqual(obj_after.to_dict(), obj_before.to_dict())


if __name__ == "__main__":
    unittest.main()

