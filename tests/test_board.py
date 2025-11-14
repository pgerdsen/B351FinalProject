import pytest

from src.game.board import Board


def make_empty_board():
    """
    Helper to construct a minimal, valid Board instance.

    Assumptions (adapt if your implementation is different):
    - `points` is a list of length 24 (one entry per point).
      We'll start with all points empty (None or 0).
    - `bar` tracks how many checkers each player has on the bar.
      We'll assume a dict with keys "X" and "O".
    - `borne_off` tracks how many checkers each player has borne off.
      Same dict structure as bar.
    """
    points = [None] * 24  # change to [0] * 24 if you use ints, etc.
    bar = {"X": 0, "O": 0}
    borne_off = {"X": 0, "O": 0}
    return Board(points, bar, borne_off)


@pytest.fixture
def empty_board():
    """Returns a fresh, empty board with 24 points and no checkers."""
    return make_empty_board()


def test_board_has_24_points(empty_board):
    """Board should have exactly 24 points."""
    # If your Board exposes points as .points, this will work directly.
    assert hasattr(empty_board, "points"), "Board should have a 'points' attribute"
    assert len(empty_board.points) == 24


def test_bar_and_borne_off_structure(empty_board):
    """
    The board should track a bar and borne-off checkers for each player.
    We only test the *shape* here, not the game rules yet.
    """
    # Bar
    assert hasattr(empty_board, "bar"), "Board should have a 'bar' attribute"
    assert isinstance(empty_board.bar, dict)
    assert set(empty_board.bar.keys()) == {"X", "O"}
    assert empty_board.bar["X"] == 0
    assert empty_board.bar["O"] == 0

    # Borne off
    assert hasattr(empty_board, "borne_off"), "Board should have a 'borne_off' attribute"
    assert isinstance(empty_board.borne_off, dict)
    assert set(empty_board.borne_off.keys()) == {"X", "O"}
    assert empty_board.borne_off["X"] == 0
    assert empty_board.borne_off["O"] == 0


def test_points_start_empty(empty_board):
    """
    In this minimal construction helper, all points start empty.
    This test just checks internal consistency of that assumption.
    """
    for p in empty_board.points:
        # If you're using None for empty points, keep this:
        assert p is None
        # If you instead use 0 or a (player, count) tuple, adjust accordingly.


@pytest.mark.skip(reason="Move logic not wired into tests yet")
def test_legal_move_updates_points_correctly():
    """
    Placeholder for when your Board has move logic (e.g. apply_move or similar).
    Marked as skipped for now so your suite passes while you implement moves.
    """
    # Example of what this might look like once you have a move API:
    #
    # board = make_empty_board()
    # board.points[0] = ("X", 2)
    #
    # board.apply_move("X", from_idx=0, to_idx=5)
    #
    # assert board.points[0] == ("X", 1)
    # assert board.points[5] == ("X", 1)
    pass


@pytest.mark.skip(reason="Game-over logic not implemented yet")
def test_game_over_detection():
    """
    Placeholder for testing game over once your Board/GameState has that logic.
    """
    # Example skeleton:
    #
    # board = make_empty_board()
    # board.borne_off["X"] = 15  # all checkers borne off
    #
    # assert board.is_game_over() is True
    # assert board.winner == "X"
    pass

