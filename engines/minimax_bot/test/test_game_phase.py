import chess
import unittest

from engines.minimax_bot.game_phase import get_num_major_and_minor_pieces, is_either_back_rank_sparse, get_game_phase, \
    GamePhase, is_middle_game, is_end_game, is_opening_game

starting_position: chess.Board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
kings_only: chess.Board = chess.Board("3k4/8/8/8/8/8/8/3K4 w - - 0 1")


class TestGamePhase(unittest.TestCase):
    def test_get_num_minor_and_major_pieces(self):
        # Given the starting board
        board = starting_position

        # When
        num_minor_and_major_pieces_1 = get_num_major_and_minor_pieces(board)

        # Then
        self.assertEqual(num_minor_and_major_pieces_1, 14)

        # Given kings only
        board = kings_only

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

    def test_is_either_back_rank_sparse(self):
        # Given
        board = starting_position
        # When
        is_sparse = is_either_back_rank_sparse(board)
        # Then
        self.assertEqual(is_sparse, False)

        # Given
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1")
        # When
        is_sparse = is_either_back_rank_sparse(board)
        # Then
        self.assertEqual(is_sparse, True)

        # Given
        board = chess.Board("rn2k3/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQq - 0 1")
        # When
        is_sparse = is_either_back_rank_sparse(board)
        # Then
        self.assertEqual(is_sparse, True)

        # Given
        board = chess.Board("rn2k3/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQq - 0 1")
        # When
        is_sparse = is_either_back_rank_sparse(board)
        # Then
        self.assertEqual(is_sparse, True)

    def test_get_game_phase(self):
        # Given
        board = starting_position
        # When
        game_phase = get_game_phase(board)
        # Then
        self.assertEqual(game_phase, GamePhase.OPENING)
        self.assertTrue(is_opening_game(board))

        # Given kings only
        board = kings_only
        # When
        game_phase = get_game_phase(board)
        # Then
        self.assertEqual(game_phase, GamePhase.END)
        self.assertTrue(is_end_game(board))

        # Given 2 pairs of minor pieces exchanged
        board = chess.Board("r1bqk2r/p1p2ppp/2p1pn2/3pB3/3PP3/8/PPP2PPP/RN1QK2R b KQkq - 0 8")
        # When
        game_phase = get_game_phase(board)
        # Then
        self.assertEqual(game_phase, GamePhase.MIDDLE)
        self.assertTrue(is_middle_game(board))

        # Given white back rank sparse
        board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1")
        # When
        game_phase = get_game_phase(board)
        # Then
        self.assertEqual(game_phase, GamePhase.MIDDLE)
        self.assertTrue(is_middle_game(board))
