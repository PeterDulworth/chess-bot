import pandas as pd
import chess
import chess.pgn
import random
import os

OPENINGS_FILE = "openings.csv"


def play_opening(board) -> tuple[str, str] | tuple[None, None]:
    candidate_moves = []

    # If we go first, randomly choose between e4 and d4
    if board.turn == chess.WHITE and board.fullmove_number == 1:
        return random.choice([("d2d4", "Queen's Pawn"), ("e2e4", "King's Pawn")])

    # Define the file path relative to the current directory.
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, OPENINGS_FILE)

    # Get all the SAN notations
    chess_openings = pd.read_csv(file_path)
    chess_openings = chess_openings["moves"].tolist()
    chess_opening_names = chess_openings["name"].tolist()

    # Loop over each opening. Try and match each position to the current game state.
    # If there is a match save the next move as a candidate move.
    opening_board = chess.Board()
    for i, opening in enumerate(chess_openings):
        opening_name = chess_opening_names[i]
        opening_moves = opening.split()

        # Loop over the moves in the opening.
        for j, move in enumerate(opening_moves):
            opening_board.push_san(move)
            try:
                # If our board matches the opening, add the next move
                if board == opening_board and opening_moves:
                    next_move = board.parse_san(opening_moves[j + 1]).uci()
                    candidate_moves.append((next_move, opening_name))
            except ValueError:
                # The opening move order ended, or move was otherwise invalid (wrong side etc.)
                break

        opening_board.reset()

    # If there are no more opening moves, return None
    if not candidate_moves:
        return None, None

    # If there is valid openings, randomly choose the next move of them
    return random.choice(candidate_moves)
