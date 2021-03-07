import unittest

from classes.room import Room

# from classes.song import Song
# from classes.bar import Bar
# from classes.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Karaoke Room 1", 8, [], [], 20, 100)

    def test_room_name(self):
        self.assertEqual("Karaoke Room 1", self.room.name)

    def test_max_capacity(self):
        self.assertEqual(8, self.room.max_capacity)

    def test_room_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room.playlist))

    def test_room_starts_empty(self):
        self.assertEqual(0, len(self.room.customers))

    def test_room_entry_fee(self):
        self.assertEqual(20, self.room.entry_fee)

    def test_room_till(self):
        self.assertEqual(100, self.room.till)


