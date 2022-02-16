import random
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

import app

number_of_random_plays = 10


def side_effect_func(value):
    return value


def random_pick_from_free_position(board):
    return random.choice(
        [int(position) for position in board if (position != 'X' and position != 'O' and position != '#')])


class TestPlayRandomGame(unittest.TestCase):
    @patch('app.player_choice')
    @patch('builtins.input')
    def test_bot_always_wins(self, input_mock: MagicMock, player_choice_mock: MagicMock):
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            for _ in range(number_of_random_plays):
                player_choice_mock.side_effect = random_pick_from_free_position
                input_mock.side_effect = [1, 1, 2, '7', '6', '8']
                app.app()
                self.assertTrue(
                    fakeOutput.getvalue().strip()[-20:] == 'X\'s player has won!!' or '  |   |\nTIE game !!!')


if __name__ == '__main__':
    unittest.main()
