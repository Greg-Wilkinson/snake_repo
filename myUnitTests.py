from unittest import TestCase
from board import Board
from getch import GetchWindows
from player import Player

class TestMethods(TestCase):


    def player_x(self):
        expected = [2, 1, 0]
        actual = Player.x
        self.assertEqual(actual, expected)