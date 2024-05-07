import chess


def get_material_eval_for_color(piece_weights, piece_counts):
    """
    Given piece counts, and piece weights, evaluate the position by calculating the material.
    """

    # TODO: add in heuristics. e.g.:
    # - Increase the weight of the rook when there are fewer pawns on the board (ours or theirs)?
    # - Decrease knight weight for each missing enemy pawn (kw = kw * (num_enemy_pawns/8))

    # White
    pawn_total = piece_counts[chess.PAWN] * piece_weights[chess.PAWN]
    rook_total = piece_counts[chess.ROOK] * piece_weights[chess.ROOK]
    knight_total = piece_counts[chess.KNIGHT] * piece_weights[chess.KNIGHT]
    bishop_total = piece_counts[chess.BISHOP] * piece_weights[chess.BISHOP]
    queen_total = piece_counts[chess.QUEEN] * piece_weights[chess.QUEEN]
    king_total = piece_counts[chess.KING] * piece_weights[chess.KING]

    return pawn_total + knight_total + bishop_total + rook_total + queen_total + king_total


def get_material_eval(board):
    """
    Given a board, evaluate the position by counting material.
    Eval = white_material - black_material.
    """

    # Value of each piece (centi-pawns)
    piece_weights = {
        chess.PAWN: 100,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 20000,
    }

    # Count the number of each piece on each side.
    white_piece_counts = dict((k, len(board.pieces((k, chess.WHITE)))) for (k, v) in piece_weights.items())
    black_piece_counts = dict((k, len(board.pieces((k, chess.BLACK)))) for (k, v) in piece_weights.items())

    # Calculate material on each side, using weights.
    white_material = get_material_eval_for_color(piece_weights, white_piece_counts)
    black_material = get_material_eval_for_color(piece_weights, black_piece_counts)

    return white_material - black_material
