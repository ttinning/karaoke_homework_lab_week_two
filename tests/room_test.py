import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Tristan", 50)
        self.song_1 = Song("Rex Orange County, New House")
        self.room_1 = Room("Room 1", [self.guest_1.name], [self.song_1.song_name])
        self.song_2 = Song("Everything Everything, Breadwinner")
        self.guest_2 = Guest("John",10)
        self.room_2 = Room("Room 2", [], [])
        self.guest_3 = Guest("Jack", 100)

    def test_room_1_has_name(self):
        expected = "Room 1"
        actual = self.room_1.room_name
        self.assertEqual(expected, actual)
    
    def test_room_1_has_song_in_room(self):
        expected = ["Rex Orange County, New House"]
        actual = self.room_1.song_list
        self.assertEqual(expected, actual)

    def test_room_1_has_guest_in_room(self):
        expected = ["Tristan"]
        actual = self.room_1.room_list
        self.assertEqual(expected, actual)

    def test_room_1_can_add_song_2_to_song_list(self):
        expected = ["Rex Orange County, New House", "Everything Everything, Breadwinner"]
        actual = self.room_1.add_song(self.song_2.song_name)
        self.assertEqual(expected, actual) 

    def test_room_1_can_add_guest_2_to_guest_list(self):
        expected = ["Tristan", "John"]
        actual = self.room_1.add_person_to_room(self.guest_2.name)
        self.assertEqual(expected, actual)

    def test_room_1_can_remove_guest(self):
        expected = []
        actual = self.room_1.remove_person_from_room(self.guest_1.name)
        self.assertEqual(expected, actual)

    def test_can_add_multiple_people_to_room(self):
        self.room_2.add_person_to_room(self.guest_2.name)
        self.room_2.add_person_to_room(self.guest_3.name)
        expected = ["John", "Jack"]
        actual = self.room_2.room_list
        self.assertEqual(expected, actual)