import chess
import numpy as np

from engines.minimax_bot.opening.opening import play_opening
from .minimax import minimax


def get_move(board, depth):
    opening_move = play_opening(board)

    if opening_move:
        print("PLAYING OPENING MOVE: ", opening_move)
        return opening_move

    top_move = None

    # Opposite of our minimax
    if board.turn == chess.WHITE:
        top_eval = -np.inf
    else:
        top_eval = np.inf

    for move in board.legal_moves:
        board.push(move)

        # WHEN WE ARE BLACK, WE WANT TRUE AND TO GRAB THE SMALLEST VALUE
        cur_eval = minimax(board, depth - 1, -np.inf, np.inf, board.turn)

        board.pop()

        if board.turn == chess.WHITE:
            if cur_eval > top_eval:
                top_move = move
                top_eval = cur_eval
        else:
            if cur_eval < top_eval:
                top_move = move
                top_eval = cur_eval

    print("CHOSEN MOVE: ", top_move, "WITH EVAL: ", top_eval)
    return top_move
