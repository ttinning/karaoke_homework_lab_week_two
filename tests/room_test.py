import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Tristan", 50)
        self.song_1 = Song("Rex Orange County, New House")
        self.room_1 = Room("Room 1", [self.guest_1.name], [self.song_1.song_name], 4)
        self.song_2 = Song("Everything Everything, Breadwinner")
        self.guest_2 = Guest("John",10)
        self.room_2 = Room("Room 2", [], [], 3)
        self.guest_3 = Guest("Jack", 100)
        self.room_3 = Room("Room 3", ["William", "Chelsea"], [], 2)

    def test_room_1_has_name(self):
        expected = "Room 1"
        actual = self.room_1.room_name
        self.assertEqual(expected, actual)
    
    def test_room_1_has_song_in_song_list(self):
        expected = ["Rex Orange County, New House"]
        actual = self.room_1.song_list
        self.assertEqual(expected, actual)

    def test_room_1_has_guest_in_room_list(self):
        expected = ["Tristan"]
        actual = self.room_1.room_list
        self.assertEqual(expected, actual)

    def test_room_1_can_add_song_2_to_song_list(self):
        expected = ["Rex Orange County, New House", "Everything Everything, Breadwinner"]
        actual = self.room_1.add_song(self.song_2.song_name)
        self.assertEqual(expected, actual) 

    def test_room_1_can_add_guest_2_to_room_list(self):
        expected = ["Tristan", "John"]
        actual = self.room_1.add_person_to_room(self.guest_2.name)
        self.assertEqual(expected, actual)

    def test_room_1_can_remove_guest_from_room_list(self):
        expected = []
        actual = self.room_1.remove_person_from_room(self.guest_1.name)
        self.assertEqual(expected, actual)
    
    def test_room_1_can_remove_guest_with_other_guest_remaining_in_room_list(self):
        self.room_1.add_person_to_room(self.guest_2.name)
        expected = ["Tristan"]
        actual = self.room_1.remove_person_from_room(self.guest_2.name)
        self.assertEqual(expected, actual)

    def test_can_add_multiple_people_to_room_list(self):
        self.room_2.add_person_to_room(self.guest_2.name)
        self.room_2.add_person_to_room(self.guest_3.name)
        expected = ["John", "Jack"]
        actual = self.room_2.room_list
        self.assertEqual(expected, actual)

    def test_room_1_has_a_room_capacity(self):
        expected = 4
        actual = self.room_1.room_capacity
        self.assertEqual(expected, actual)

    def test_room_3_can_not_take_more_guests_than_its_capacity(self):
        self.room_3.add_person_to_room(self.guest_2.name)
        expected = ["William", "Chelsea"]
        actual = self.room_3.room_list
        self.assertEqual(expected, actual)

    def test_room_1_can_add_money_to_update_till_total(self):
        expected = 120
        actual = self.room_1.add_money_to_till(20)
        self.assertEqual(expected, actual)
