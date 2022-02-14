import unittest
from unittest.mock import MagicMock, patch

import app
import utils

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
    def test_game_participant_sad_path_insert_string_instead_of_int(self, input_mock: MagicMock):
        input_mock.side_effect = ['k', 'h', 1]
        res = utils.game_participants()
        self.assertEqual(res, 1)

    @patch('builtins.input')
    def test_choose_marks_sad_path_insert_string_instead_of_int(self, input_mock: MagicMock):
        input_mock.side_effect = ['k', '1']
        res = utils.choose_marks()
        self.assertEqual(res, {'player1_mark': 'X', 'player2_mark': 'O'})

    @patch('builtins.input')
    def test_player_choice_sad_path_insert_string_instead_of_int(self, input_mock: MagicMock):
        input_mock.side_effect = ['k', '1']
        res = utils.player_choice([' ']*10)
        self.assertEqual(res, 1)

    @patch('builtins.input')
    def test_reply_sad_path_insert_string_instead_of_int(self, input_mock: MagicMock):
        input_mock.side_effect = ['k', '1']
        res = utils.reply()
        self.assertEqual(res, 1)



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
    def test_choose_marks_happy_path_option_1(self, input_mock: MagicMock):
        input_mock.return_value = 1
        res = app.choose_marks()
        self.assertEqual(res, {'player1_mark': 'X',
                               'player2_mark': 'O'})

    @patch('builtins.input')
    def test_choose_marks_happy_path_opotin_2(self, input_mock: MagicMock):
        input_mock.return_value = 2
        res = app.choose_marks()
        self.assertEqual(res, {'player1_mark': 'O',
                               'player2_mark': 'X'})

    def test_space_check_free_spot(self):
        board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        res = utils.space_check(board, 3)
        self.assertTrue(res)

    def test_space_check_ccupied_spot_x_mark(self):
        board = ['#', '1', '2', 'X', '4', '5', '6', '7', '8', '9']
        res = utils.space_check(board, 3)
        self.assertFalse(res)

    def test_space_check_ccupied_spot_O_mark(self):
        board = ['#', '1', '2', 'X', 'O', '5', '6', '7', '8', '9']
        res = utils.space_check(board, 4)
        self.assertFalse(res)






if __name__ == '__main__':
    unittest.main()
