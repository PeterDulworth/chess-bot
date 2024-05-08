import chess
import unittest

from engines.minimax_bot.game_phase import get_num_major_and_minor_pieces


class TestGamePhase(unittest.TestCase):
    def test_get_num_minor_and_major_pieces(self):
        # Given the starting board
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

        # When
        num_minor_and_major_pieces = get_num_major_and_minor_pieces(board)

        # Then
        self.assertEqual(num_minor_and_major_pieces, 14)
