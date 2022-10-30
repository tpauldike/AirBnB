#!/usr/bin/env python3
# test_state.py

""" Defines the unittests for state.py

    Unittest classes:
        TestState_instantiation
        TestState_methods
"""
import unittest
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """ Unittests for testing the instantiation of the State class """

    def test_obj_is_state(self):
        self.assertIsInstance(State(), State)

    def test_called_with_kwargs(self):
        s1 = State()
        s1_dict = s1.to_dict()
        s2 = State(**s1_dict)
        self.assertEqual(str(s2), str(s1))

    def test_has_attr(self):
        pass
