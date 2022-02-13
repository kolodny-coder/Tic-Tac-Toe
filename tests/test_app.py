import app
from unittest.mock import MagicMock, patch
import unittest
import utils
from io import StringIO

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
        result = app.minmax(['#', ' ', ' ', ' ', ' ', 'O', ' ', 'X', ' ', 'X'], 0, True, 'X', 'O')
        self.assertEqual(result, 100)

    def test_minmax_x_wins2(self):
        result = app.minmax(['#', 'X', ' ', 'O', ' ', 'O', ' ', ' ', ' ', 'X'], 0, True, 'X', 'O')
        self.assertEqual(result, 100)

    def test_minmax_o_wins(self):
        result = app.minmax(['#', 'X', ' ', 'O', ' ', 'X', ' ', ' ', 'O', ' '], 0, False, 'X', 'O')
        self.assertEqual(result, -100)

    def test_minmax_draw(self):
        result = app.minmax(['#', 'X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X'], 0, True, 'X', 'O')
        self.assertEqual(result, 0)

    def test_minmax_draw2(self):
        result = app.minmax(['#', 'X', 'O', 'O', 'O', 'O', ' ', 'X', ' ', 'X'], 0, True, 'X', 'O')
        self.assertEqual(result, 100)


    @patch('builtins.input')
    def test_game_participants(self, input_mock: MagicMock):
        with self.subTest('test game participants function happy path'):
            for choose_option in [1, 2, 3]:
                input_mock.return_value = choose_option
                res = utils.game_participants()
                self.assertEqual(res, choose_option)

    @patch('builtins.input')
    def test_choose_marks(self, input_mock: MagicMock):
        with self.subTest('test game choose marks function happy path option 1'):
            input_mock.return_value = 1
            res = utils.choose_marks()
            self.assertEqual(res, {'player1_mark': 'X', 'player2_mark': 'O'})

        with self.subTest('test game choose marks function happy path option 2'):
                input_mock.return_value = 2
                res = utils.choose_marks()
                self.assertEqual(res, {'player1_mark': 'O',
                                       'player2_mark': 'X'})


    @patch('builtins.input')
    def test_game_participants_printeed(self, input_mock: MagicMock):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            input_mock.return_value = 1
            app.app()
            input_mock.return_value = 1
            self.assertEqual(fakeOutput.getvalue().strip()[0], 'human vs human')





if __name__ == '__main__':
    unittest.main()
