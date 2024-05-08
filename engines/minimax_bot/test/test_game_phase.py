import chess
import unittest

from engines.minimax_bot.game_phase import get_num_major_and_minor_pieces


class TestGamePhase(unittest.TestCase):
    def test_get_num_minor_and_major_pieces(self):
        # Given the starting board
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")

        # When
        num_minor_and_major_pieces_1 = get_num_major_and_minor_pieces(board)

        # Then
        self.assertEqual(num_minor_and_major_pieces_1, 14)

        # Given kings only
        board = chess.Board("3k4/8/8/8/8/8/8/3K4 w - - 0 1")

        # When
        num_minor_and_major_pieces_2 = get_num_major_and_minor_pieces(board)

        # Then
        self.assertEqual(num_minor_and_major_pieces_2, 0)

        # Given kings and queens
        board = chess.Board("q2k4/8/8/8/8/8/8/Q2K4 w - - 0 1")

        # When
        num_minor_and_major_pieces_2 = get_num_major_and_minor_pieces(board)

        # Then
        self.assertEqual(num_minor_and_major_pieces_2, 2)

