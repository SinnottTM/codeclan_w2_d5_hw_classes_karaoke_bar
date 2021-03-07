import unittest

from classes.song import Song

# from classes.room import Room
# from classes.guest import Guest
# from classes.bar import Bar

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("I Wanta Rock", "Twisted Sister")

    def test_song_name(self):
        self.assertEqual("I Wanta Rock", self.song.name)

    def test_song_artist(self):
        self.assertEqual("Twisted Sister", self.song.artist)
