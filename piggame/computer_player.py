from .player import Player

class ComputerPlayer(Player):
    """A computer-controlled player.

    Strategy:
      Hold at min(25, 100 - current_score); otherwise, roll again.
    """

    def decide(self, turn_total: int) -> str:
        hold_at = min(25, 100 - self.score)
        return "hold" if turn_total >= hold_at else "roll"
