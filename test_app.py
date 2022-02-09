import app
from unittest import mock
import unittest

test_board_cross_the_top = ['#', 'X', 'X', 'X', '4', '5', '6', '7', '8', '9']
test_board_cross_the_middle = ['#', '1', '2', '3', 'X', 'X', 'X', '7', '8', '9']
test_board_cross_the_bottom = ['#', 'X', '2', '3', '4', '5', '6', 'X', 'X', 'X']

test_board_down_the_left = ['#', 'X', 'X', 'X', '4', '5', '6', 'X', '8', '9']
test_board_down_the_middle = ['#', '1', 'X', '3', '4', 'X', '6', '7', 'X', '9']
test_board_down_the_right = ['#', 'X', '2', '3', '4', '5', '6', 'X', 'X', 'X']

test_board_diagonal_left_to_right = ['#', 'X', '2', '3', '4', 'X', '6', '7', '8', 'X']
test_board_diagonal_right_to_left = ['#', '1', '2', 'X', '4', 'X', '6', 'X', '3', 'X']


class TestStringMethods(unittest.TestCase):

    def test_check_for_win_cross_the_top(self):
        result = app.check_for_win(test_board_cross_the_top, 'X')
        self.assertTrue(result)

    def test_check_for_win_cross_the_middle(self):
        result = app.check_for_win(test_board_cross_the_middle, 'X')
        self.assertTrue(result)

    def test_check_for_win_cross_the_bootom(self):
        result = app.check_for_win(test_board_cross_the_bottom, 'X')
        self.assertTrue(result)

    def test_check_for_win_down_the_left(self):
        result = app.check_for_win(test_board_down_the_left, 'X')
        self.assertTrue(result)

    def test_check_for_win_dowm_the_middle(self):
        result = app.check_for_win(test_board_down_the_middle, 'X')
        self.assertTrue(result)

    def test_check_for_win_dowm_the_right(self):
        result = app.check_for_win(test_board_down_the_right, 'X')
        self.assertTrue(result)

    def test_check_for_win_diagonal_left_to_right(self):
        result = app.check_for_win(test_board_diagonal_right_to_left, 'X')
        self.assertTrue(result)

    def test_check_for_win_diagonal_right_to_left(self):
        result = app.check_for_win(test_board_diagonal_left_to_right, 'X')
        self.assertTrue(result)

    def test_minmax_x_wins(self):
        result = app.minmax(['#', '1', '2', 'X', '4', '0', '6', 'X', '3', 'X'], 0, True)
        self.assertEqual(result, 100)

    def test_minmax_x_wins2(self):
        result = app.minmax(['#', 'X', ' ', 'O', ' ', 'O', ' ', ' ', ' ', 'X'], 0, True)
        self.assertEqual(result, 100)

    def test_minmax_o_wins(self):
        result = app.minmax(['#', '1', '2', 'O', '4', '0', '6', 'O', '3', 'O'], 0, True)
        self.assertEqual(result, -100)

    def test_minmax_draw(self):
        result = app.minmax(['#', 'X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X'], 0, True)
        self.assertEqual(result, 0)

    def test_minmax_draw2(self):
        result = app.minmax(['#', 'X', 'O', 'O', 'O', 'O', ' ', 'X', ' ', 'X'], 0, True)
        self.assertEqual(result, 100)

    def test_comp_move(self):
        result = app.comp_move(['#', 'X', 'O', ' ', 'X', 'O', 'O', ' ', 'X', 'X'])
        self.assertEqual(result, 0)

    def test_game_participents(self):
        with mock.patch('builtins.input', return_value=1):
            assert game_participents() == 1

        with mock.patch('builtins.input', return_value=2):
            assert game_participents() == 2

        # with mock.patch('builtins.input', return_value="no"):
        #     assert yes_or_no() == "Awesome!"


if __name__ == '__main__':
    unittest.main()
