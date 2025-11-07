from .player import HumanPlayer
from .computer_player import ComputerPlayer

class PlayerFactory:
    """Factory to create different player types."""

    @staticmethod
    def create(kind: str, name: str):
        kind = (kind or "").strip().lower()
        if kind == "human":
            return HumanPlayer(name)
        elif kind == "computer":
            return ComputerPlayer(name)
        raise ValueError(f"Unknown player type: {kind}")
