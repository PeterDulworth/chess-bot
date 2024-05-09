"""
Implementation the MINIMAX algorithm, with alpha-beta pruning.
Based on explanation in this video: https://www.youtube.com/watch?v=l-hh51ncgDI

MiniMax: based on depth-first-search (DFS).

If all positions are accurately evaluated, then minimax returns the objective best move.

"""

import numpy as np
import chess
from engines.minimax_bot.evaluate.evaluate import get_evaluation


def minimax(board: chess.Board, depth: int, alpha: float, beta: float, maximizing_player: chess.Color):
    # Base case (one of):
    # - If we have reached a leaf node (for our depth)
    # - If we have reached the end of the game
    if depth == 0 or board.is_game_over():
        return get_evaluation(board)

    # If it's the maximizing players turn (white), loop through each child and recursively call
    # search (with depth - 1, and turn passed to black).
    if maximizing_player:
        max_eval = -np.inf
        for move in board.legal_moves:
            board.push(move)
            cur_eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, cur_eval)
            alpha = max(alpha, cur_eval)
            if beta <= alpha:
                break
        return max_eval

    # If it's the minimizing players turn (black), do the same thing but minimize instead of maximize.
    else:
        min_eval = np.inf
        for move in board.legal_moves:
            board.push(move)
            cur_eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, cur_eval)
            beta = min(beta, cur_eval)
            if beta <= alpha:
                break
        return min_eval
