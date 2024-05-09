import chess
import numpy as np
import logging

from engines.minimax_bot.opening.opening import play_opening
from engines.minimax_bot.search.minimax import minimax

logger = logging.getLogger(__name__)


def get_move(board, depth):
    opening_move, opening_name = play_opening(board)

    if opening_move:
        logger.info(f"Playing book move 📚: {opening_move}. Opening={opening_name}")
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

    logger.info(f"Playing engine move 🤖: {top_move}, eval={top_eval / 100.0}")
    return top_move
