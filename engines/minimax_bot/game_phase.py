"""
Detect which phase of the game we are in: Beginning, middle, end.
"""

from enum import StrEnum


class GamePhase(StrEnum):
    EARLY = "early"
    MIDDLE = "middle"
    END = "end"


def get_game_phase():
    pass


def is_early_game():
    return get_game_phase() == GamePhase.EARLY


def is_middle_game():
    return get_game_phase() == GamePhase.MIDDLE


def is_end_game():
    return get_game_phase() == GamePhase.END