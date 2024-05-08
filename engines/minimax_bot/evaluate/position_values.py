"""
Weights assigned to each piece based on the square it occupies.
Based on SEF: https://www.chessprogramming.org/Simplified_Evaluation_Function.

These values are from whites perspective. Mirror vertically for blacks perspective.
"""
import chess

from engines.minimax_bot.game_phase import GamePhase

position_weights: dict[chess.Piece, list[int]] = {
    chess.PAWN: [
        0,   0,  0,   0,   0,   0,   0,  0,
        50,  50, 50,  50,  50,  50,  50, 50,
        10,  10, 20,  30,  30,  20,  10, 10,
        5,   5,  10,  25,  25,  10,  5,  5,
        0,   0,  0,   20,  20,  0,   0,  0,
        5,  -5, -10,  0,   0,  -10, -5,  5,
        5,   10, 10, -20, -20,  10,  10, 5,
        0,   0,  0,   0,   0,   0,   0,  0
    ],
    chess.KNIGHT: [
        -50, -40, -30, -30, -30, -30, -40, -50,
        -40, -20,  0,   0,   0,   0,  -20, -40,
        -30,  0,   10,  15,  15,  10,  0,  -30,
        -30,  5,   15,  20,  20,  15,  5,  -30,
        -30,  0,   15,  20,  20,  15,  0,  -30,
        -30,  5,   10,  15,  15,  10,  5,  -30,
        -40, -20,  0,   5,   5,   0,  -20, -40,
        -50, -40, -30, -30, -30, -30, -40, -50,
    ],
    chess.BISHOP: [
        -20, -10, -10, -10, -10, -10, -10, -20,
        -10,  0,   0,   0,   0,   0,   0,  -10,
        -10,  0,   5,   10,  10,  5,   0,  -10,
        -10,  5,   5,   10,  10,  5,   5,  -10,
        -10,  0,   10,  10,  10,  10,  0,  -10,
        -10,  10,  10,  10,  10,  10,  10, -10,
        -10,  5,   0,   0,   0,   0,   5,  -10,
        -20, -10, -10, -10, -10, -10, -10, -20,
    ],
    chess.ROOK: [
         0, 0,  0,  0,  0,  0,  0,  0,
         5, 10, 10, 10, 10, 10, 10, 5,
        -5, 0,  0,  0,  0,  0,  0, -5,
        -5, 0,  0,  0,  0,  0,  0, -5,
        -5, 0,  0,  0,  0,  0,  0, -5,
        -5, 0,  0,  0,  0,  0,  0, -5,
        -5, 0,  0,  0,  0,  0,  0, -5,
         0, 0,  0,  5,  5,  0,  0,  0
    ],
    chess.QUEEN: [
        -20, -10, -10, -5, -5, -10, -10, -20,
        -10,  0,   0,   0,  0,  0,   0,  -10,
        -10,  0,   5,   5,  5,  5,   0,  -10,
        -5,   0,   5,   5,  5,  5,   0,  -5,
         0,   0,   5,   5,  5,  5,   0,  -5,
        -10,  5,   5,   5,  5,  5,   0,  -10,
        -10,  0,   5,   0,  0,  0,   0,  -10,
        -20, -10, -10, -5, -5, -10, -10, -20
    ],
    chess.KING: [
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -30, -40, -40, -50, -50, -40, -40, -30,
        -20, -30, -30, -40, -40, -30, -30, -20,
        -10, -20, -20, -20, -20, -20, -20, -10,
         20,  20,  0,   0,   0,   0,   20,  20,
         20,  30,  10,  0,   0,   10,  30,  20
    ],
}

# endgame weights are the same, except the king is rewarded for being in the center of the board
position_weights_endgame: dict[chess.Piece, list[int]] = position_weights.copy()
position_weights_endgame[chess.KING] = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10,  0,   0,  -10, -20, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -30,  0,   0,   0,   0,  -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50
]


def get_position_weights(game_phase: GamePhase) -> dict[chess.Piece, list[int]]:
    if game_phase == GamePhase.END:
        return position_weights_endgame
    else:
        return position_weights
