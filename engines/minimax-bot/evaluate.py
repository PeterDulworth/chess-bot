from piece_values import get_material_eval
import chess
import position_values

pieces = [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]


def get_evaluation(board):
    """
    Given a board, evaluate the position.
    """
    # Handle checkmate / stalemate.
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

    # Count the material. Material = white - black.
    material_eval = get_material_eval(board)

    # Count the values of each piece based on it's position on the board.
    # TODO: detect middle game vs end game and use appropriate weights for kings
    positional_eval = 0
    for piece in pieces:
        positional_eval += sum([position_values.position_weights[piece][i] for i in board.pieces(piece, chess.WHITE)])

    for piece in pieces:
        positional_eval -= sum([position_values.position_weights[piece][chess.square_mirror(i)] for i in board.pieces(piece, chess.BLACK)])

    return material_eval + positional_eval
