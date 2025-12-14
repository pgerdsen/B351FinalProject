"""
Main entry point for graphical backgammon UI.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Add src to path if needed
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from game.state import GameState
from ui.graphical import GraphicalUI


def main():
    """Start the graphical backgammon game."""
    state = GameState.initial()
    ui = GraphicalUI(state)
    ui.run()


if __name__ == "__main__":
    main()

