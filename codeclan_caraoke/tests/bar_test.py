import unittest

from classes.bar import Bar

# from classes.room import Room
# from classes.guest import Guest
# from classes.song import Song

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("The Mighty Session", [1,2,3,4], 20.00, [], 32)

    def test_bar_name(self):
        self.assertEqual("The Mighty Session", self.bar.name)

    def test_bar_rooms(self):
        self.assertEqual(4, len(self.bar.karaoke_rooms))

    def test_bar_entry_price(self):
        self.assertEqual(20.00, self.bar.entry_price)

    def test_bar_lobby_empty(self):
        self.assertEqual(0, len(self.bar.lobby))

    def test_bar_total_guests(self):
        self.assertEqual(32, self.bar.total_guests)
