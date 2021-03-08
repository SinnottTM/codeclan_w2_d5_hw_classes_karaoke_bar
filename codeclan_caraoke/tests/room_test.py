import unittest

from classes.room import Room
from classes.song import Song
from classes.bar import Bar
from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("codeclan_caraoke_room_1", 8, [], [])

        self.guest1 = Guest("Tim Sinnott", 50, "The Passanger", "Iggy Pop")
        self.guest2 = Guest("Richard Duffy", 100, "Better Man", "Pearl Jam")
        self.guest3 = Guest("Dani Kavanagh", 0, "Piano Man", "Billy Joel")
        self.song1 = Song("Crazy Train", "Ozzy Ozbourne")
        self.song2 = Song("The Passanger", "Iggy Pop")
        self.song3 = Song("Better Man", "Pearl Jam")

        self.bar = Bar("The Mighty Session", [self.room], 25, 0, [], 0, ["Guinness", "Cava", "Corona"])

    def test_room_name(self):
        self.assertEqual("codeclan_caraoke_room_1", self.room.name)

    def test_max_capacity(self):
        self.assertEqual(8, self.room.max_capacity)

    def test_room_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room.playlist))

    def test_room_starts_empty(self):
        self.assertEqual(0, len(self.room.guests))

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(self.guest1)
        self.assertEqual(1, len(self.room.guests))

    def test_add_guest_to_room_max_capacity(self):
        self.room.guests = [self.guest1, self.guest2, self.guest3, self.guest1, self.guest2, self.guest3, self.guest1, self.guest2]
        self.room.add_guest_to_room(self.guest3)
        self.assertEqual(8, len(self.room.guests))

    def test_remove_guest_from_room(self):
        self.room.guests = [self.guest1, self.guest2]
        self.room.remove_guest_from_room(self.guest1, self.bar)
        self.assertEqual(1, len(self.room.guests))

    def add_new_song_to_playlist_(self):
        self.room.add_new_song_to_playlist(self.song1)
        self.assertEqual(self.song1, self.room.playlist[0])

    def test_length_of_playlist(self):
        self.room.playlist = [self.song1, self.song2]
        self.assertEqual(2, len(self.room.playlist))

    def test_remove_song_from_playlist(self):
        self.room.playlist = [self.song1, self.song2]
        self.room.remove_song_from_playlist(self.song2)
        self.assertEqual(1, len(self.room.playlist))

    def test_check_favourite_song_present(self):
        self.room.guests = [self.guest1, self.guest2]
        self.room.playlist = [self.song1, self.song2, self.song3]
        self.assertEqual("Oh I love this song!",self.room.check_favourite_song(self.guest2))

    def test_check_favourite_song_not_present(self):
        self.room.guests = [self.guest1, self.guest2]
        self.room.playlist = [self.song1, self.song2]
        self.assertEqual("This place sucks!",self.room.check_favourite_song(self.guest2))
