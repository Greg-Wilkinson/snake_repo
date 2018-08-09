from unittest import TestCase
from board import Board
from getch import GetchWindows

class TestMethods(TestCase):

    def test_height_and_width_input_are_more_than_5(self):
        width = 4
        height = 3
        testBoard = Board(width, height)
        actual = [testBoard.width, testBoard.height]
        expected = [6, 6]
        self.assertEqual(actual, expected)

    def getch_receives_characters(self):
            self.assertEqual(GetchWindows.__call__(), "a")
