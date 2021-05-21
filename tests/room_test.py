import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 1")
        self.room_2 = Room("Room 2")

    def test_room_1_has_name(self):
        expected = "Room 1"
        actual = self.room_1.name
        self.assertEqual(expected, actual)