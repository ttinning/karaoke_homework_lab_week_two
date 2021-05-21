import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Tristan")
        self.guest_2 = Guest("Clayre")

    def test_guest_1_has_name(self):
        expected = "Tristan"
        actual = self.guest_1.name
        self.assertEqual(expected, actual)

    def test_guest_2_has_name(self):
        expected = "Clayre"
        actual = self.guest_2.name
        self.assertEqual(expected, actual)
