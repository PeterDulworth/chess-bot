"""
Detect which phase of the game we are in: opening, middle, end.
"""

from enum import StrEnum
import chess


class GamePhase(StrEnum):
    OPENING = "opening"
    MIDDLE = "middle"
    END = "end"


def get_num_major_and_minor_pieces(board: chess.Board):
    bishops = len(board.pieces(chess.BISHOP, chess.WHITE)) + len(board.pieces(chess.BISHOP, chess.BLACK))
    knights = len(board.pieces(chess.KNIGHT, chess.WHITE)) + len(board.pieces(chess.KNIGHT, chess.BLACK))
    rooks = len(board.pieces(chess.ROOK, chess.WHITE)) + len(board.pieces(chess.ROOK, chess.BLACK))
    queens = len(board.pieces(chess.QUEEN, chess.WHITE)) + len(board.pieces(chess.QUEEN, chess.BLACK))
    return bishops + knights + rooks + queens


def is_either_back_rank_sparse(board: chess.Board):
    """
    We say the back-rank is sparse if the "owning" color, has less than 4 pieces on it.
    e.g. for white: if the 1st rank has less than 4 white pieces, then the back-rank is sparse.

    This function returns true if EITHER back rank is sparse.
    """
    # list of pieces on each back rank
    white_back_rank = board.piece_map(mask=chess.BB_RANKS[0]).values()
    black_back_rank = board.piece_map(mask=chess.BB_RANKS[7]).values()

    # list of pieces of corresponding color on back rank
    white_pieces_on_white_back_rank = list(filter(lambda p: p.color == chess.WHITE, white_back_rank))
    black_pieces_on_black_back_rank = list(filter(lambda p: p.color == chess.BLACK, black_back_rank))

    return len(white_pieces_on_white_back_rank) < 4 or len(black_pieces_on_black_back_rank) < 4


def get_game_phase(board: chess.Board):
    """
    Opening: starts on move 1.

    Mid-game (any of the following):
        - There are less than 11 major + minor pieces on the board
        - There are less than 4 pieces of the corresponding color on the back rank for either color

    End-game:
        - when there are less than 7 minor and major pieces on the board the
          end-game has begun (so, perhaps 2 rooks and a bishop Vs 2 bishops and a knight).
    """

    num_major_and_minor_pieces = get_num_major_and_minor_pieces(board)

    if num_major_and_minor_pieces < 7:
        return GamePhase.END
    elif num_major_and_minor_pieces < 11 or is_either_back_rank_sparse(board):
        return GamePhase.MIDDLE
    else:
        return GamePhase.OPENING


def is_opening_game(board: chess.Board):
    return get_game_phase(board) == GamePhase.OPENING


def is_middle_game(board: chess.Board):
    return get_game_phase(board) == GamePhase.MIDDLE


def is_end_game(board: chess.Board):
    return get_game_phase(board) == GamePhase.END
