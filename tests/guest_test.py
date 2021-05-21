import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Tristan", 50)
        self.guest_2 = Guest("Clayre", 200)

    def test_guest_1_has_name(self):
        expected = "Tristan"
        actual = self.guest_1.name
        self.assertEqual(expected, actual)

    def test_guest_2_has_name(self):
        expected = "Clayre"
        actual = self.guest_2.name
        self.assertEqual(expected, actual)

    def test_guest_1_has_money(self):
        expected = 50
        actual = self.guest_1.wallet
        self.assertEqual(expected,actual)

    def test_guest_2_has_money(self):
        expected = 200
        actual = self.guest_2.wallet
        self.assertEqual(expected, actual)

    def test_remove_cash_from_guest_1_wallet(self):
        expected = 40
        actual = self.guest_1.remove_cash(10)
        self.assertEqual(expected, actual)
