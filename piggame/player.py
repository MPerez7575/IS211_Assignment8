class Player:
    """Base player class used for both humans and computers."""

    def __init__(self, name: str):
        self.name = name
        self.score = 0

    def decide(self, turn_total: int) -> str:
        """Ask human player if they want to roll or hold."""
        while True:
            choice = input(f"{self.name}, roll or hold? (r/h): ").strip().lower()
            if choice in ("r", "roll"):
                return "roll"
            if choice in ("h", "hold"):
                return "hold"
            print("Invalid choice, please type 'r' or 'h'.")


class HumanPlayer(Player):
    """Same as Player, separated for Factory pattern clarity."""
    pass
