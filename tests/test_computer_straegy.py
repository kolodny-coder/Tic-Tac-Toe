import unittest

from computer_strategy import comp_return_position


class TestStringMethods(unittest.TestCase):

    def test_center_response_strategy(self):
        result = comp_return_position([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        self.assertEqual(result, 1)

    def test_center_response_strategy_2nd_move(self):
        result = comp_return_position([' ', 'X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' '])
        self.assertEqual(result, 9)

    # Player Second Move

    def test_center_response_strategy_3rd_move1(self):
        result = comp_return_position([' ', 'X', ' ', 'O', ' ', 'O', ' ', ' ', ' ', 'X'])
        self.assertEqual(result, 7)

    def test_center_response_strategy_3rd_move2(self):
        result = comp_return_position([' ', 'X', ' ', ' ', ' ', 'O', ' ', 'O', ' ', 'X'])
        self.assertEqual(result, 3)

    def test_center_response_strategy_player_plays_position_2_on_his_second_move(self):
        result = comp_return_position([' ', 'X', 'O', ' ', ' ', 'O', ' ', ' ', ' ', 'X'])
        self.assertEqual(result, 7)

    def test_center_response_strategy_player_plays_position_4_on_his_second_move(self):
        result = comp_return_position([' ', 'X', ' ', ' ', 'O', 'O', ' ', ' ', ' ', 'X'])
        self.assertEqual(result, 6)

    def test_center_response_strategy_player_plays_position_6_on_his_second_move(self):
        result = comp_return_position([' ', 'X', ' ', ' ', ' ', 'O', 'O', ' ', ' ', 'X'])
        self.assertEqual(result, 4)

    # Computer lands winning move
    def test_center_response_winner_move_player_played_postion_2(self):
        result = comp_return_position([' ', 'X', 'O', 'O', ' ', 'O', ' ', 'X', ' ', 'X'])
        self.assertEqual(result, 8)

    def test_center_response_winner_move_player_played_postion_4(self):
        result = comp_return_position([' ', 'X', ' ', 'O', 'O', 'O', ' ', 'X', ' ', 'X'])
        self.assertEqual(result, 8)

    def test_center_response_winner_move_player_played_postion_6(self):
        result = comp_return_position([' ', 'X', ' ', 'O', ' ', 'O', 'O', 'X', ' ', 'X'])
        self.assertEqual(result, 8)

    def test_center_response_winner_move_player_played_postion_8(self):
        result = comp_return_position([' ', 'X', ' ', 'O', ' ', 'O', ' ', 'X', 'O', 'X'])
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
