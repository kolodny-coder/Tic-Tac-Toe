import random
import unittest
from unittest.mock import MagicMock, patch
from io import StringIO

import app


def side_effect_func(value):
    return value


def random_pick_from_free_position(board):
    return random.choice(
        [position for position in board if (position != 'X' and position != 'O' and position != '#')])


class TestStringMethods(unittest.TestCase):
    @patch('utils.player_choice')
    @patch('builtins.input')
    def test_bot_always_wins(self, input_mock: MagicMock, player_choice_mock: MagicMock):
        for _ in range(10):

            with patch('sys.stdout', new=StringIO()) as fakeOutput:
                player_choice_mock.side_effect = random_pick_from_free_position
                input_mock.side_effect = [1, 1, 2, '5', '6', '8']
                app.app()

                self.assertEqual(fakeOutput.getvalue().strip()[-20:], 'X\'s player has won!!')


if __name__ == '__main__':
    unittest.main()
