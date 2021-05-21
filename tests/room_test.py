import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Tristan")
        self.song_1 = Song("Rex Orange County", "New House")
        self.room_1 = Room("Room 1", [self.guest_1.name], [
            {"artist_name": self.song_1.artist_name,
            "song_name": self.song_1.song_name}
        ])
    

    def test_room_1_has_name(self):
        expected = "Room 1"
        actual = self.room_1.name
        self.assertEqual(expected, actual)
    
    def test_room_1_has_song_in_room(self):
        expected = [{"artist_name": "Rex Orange County", "song_name": "New House"}]
        actual = self.room_1.song_list
        self.assertEqual(expected, actual)

    def test_room_1_has_guest_in_room(self):
        expected = ["Tristan"]
        actual = self.room_1.guest_list
        self.assertEqual(expected, actual)