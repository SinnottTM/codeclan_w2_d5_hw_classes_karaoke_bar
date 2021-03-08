import unittest

from classes.guest import Guest

# from classes.bar import Bar
# from classes.room import Room
# from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Zsolt P-S", 1000,"No One Like You", "The Scorpions")

    def test_guest_name(self):
        self.assertEqual("Zsolt P-S", self.guest.name)

    def test_guest_wallet(self):
        self.assertEqual(1000, self.guest.wallet)
    
    def test_guest_song_artist_song(self): 
        self.assertEqual("No One Like You", self.guest.favourite_song_artist_song)

    def test_guest_song_artist_name(self):
        self.assertEqual("The Scorpions",self.guest.favourite_song_artist_name)
