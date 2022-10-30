#!/usr/bin/env python3
# test_user.py

""" Defines  unittests for user.py

    Unittests classes:
        TestUser_instantiation
        TestUser_inherited_methods
"""
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel

class TestUser_instantiation(unittest.TestCase):
    """ Unittest for testing the instantiation of the User class. """

    def test_obj_is_user(self):
        self.assertIsInstance(User(), User)

    def test_no_args(self):
        self.assertIsInstance(User(), User)

    def test_with_kwargs(self):
        u = User()
        u_dict = u.to_dict()
        u_new = User(**u_dict)
        self.assertEqual(u.id, u_new.id)

    def test_has_id(self):
        user1 = User()
        user2 = User()
        self.assertEqual(type(User().id), str)
        self.assertEqual(type(user1.id), type(user2.id))
        self.assertNotEqual(user1.id, user2.id)

    def test_has_created_at(self):
        user1 = User()
        user2 = User()
        self.assertIsInstance(user1.created_at, datetime)
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_has_updated_at(self):
        user1 = User()
        user2 = User()
        self.assertIsInstance(user1.updated_at, datetime)
        self.assertNotEqual(user1.updated_at, user2.updated_at)

    def test_has_email(self):
        user1 = User()
        self.assertIsInstance(user1.email, str)

    def test_has_password(self):
        user1 = User()
        self.assertIsInstance(user1.password, str)

    def test_has_first_name(self):
        user1 = User()
        self.assertIsInstance(user1.first_name, str)

    def test_has_last_name(self):
        user1 = User()
        self.assertIsInstance(user1.last_name, str)

    def test_sub_class(self):
        self.assertTrue(issubclass(User, BaseModel))


class TestUser_methods(unittest.TestCase):
    """ Unittests for the methods that are inherited by User class """

    def test_user_to_dict(self):
        u = User()
        u.email = "email@email.com"
        u.last_name = "my_last_name"
        u_dict = u.to_dict()
        self.assertIsInstance(u.to_dict(), dict)
        self.assertEqual(u_dict["id"], u.id)
        self.assertEqual(u_dict["__class__"], u.__class__.__name__)
        self.assertEqual(u_dict["created_at"], u.created_at.isoformat())
        self.assertEqual(u_dict["updated_at"], u.updated_at.isoformat())
        self.assertEqual(u_dict["email"], u.email)
        self.assertEqual(u_dict["last_name"], u.last_name)
