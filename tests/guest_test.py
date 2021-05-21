import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Tristan")

    def test_guest_has_name(self):
        expected = "Tristan"
        actual = self.guest.name
        self.assertEqual(expected, actual)
