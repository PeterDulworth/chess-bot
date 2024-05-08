import numpy as np
from engines.minimax_bot.evaluate.evaluate import get_evaluation


def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return get_evaluation(board)

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
