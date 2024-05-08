from engines.minimax_bot.evaluate.piece_values import get_material_eval
import chess
from engines.minimax_bot.evaluate.position_values import get_position_weights
from engines.minimax_bot.game_phase import get_game_phase

pieces = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]


def get_evaluation(board):
    """
    Given a board, evaluate the position.
    """
    # Handle checkmate / stalemate.
    if board.is_checkmate():
        if board.turn == chess.WHITE:
            return -99999
        else:
            return 99999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    # Count the material. Material = white - black.
    material_eval = get_material_eval(board)

    # Count the values of each piece based on it's position on the board.
    # Use different weights depending on game-phase.
    position_weights = get_position_weights(game_phase=get_game_phase(board))
    positional_eval = 0
    for piece in pieces:
        positional_eval += sum([position_weights[piece][i] for i in board.pieces(piece, chess.WHITE)])

    for piece in pieces:
        positional_eval -= sum([position_weights[piece][chess.square_mirror(i)] for i in board.pieces(piece, chess.BLACK)])

    return material_eval + positional_eval
