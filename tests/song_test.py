import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Rex Orange County, New House")
        self.song_2 = Song("Tyler, The Creator, EARFQUAKE")
    
    def test_song_1_has_song_name(self):
        expected = "Rex Orange County, New House"
        actual = self.song_1.song_name
        self.assertEqual(expected, actual)

    def test_song_2_has_song_name(self):
        expected = "Tyler, The Creator, EARFQUAKE"
        actual = self.song_2.song_name
        self.assertEqual(expected, actual)