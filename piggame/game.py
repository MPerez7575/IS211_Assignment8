from .die import Die

class Game:
    """Handles the turn logic for the Pig Dice Game."""

    def __init__(self, player1, player2, target=100, seed=None):
        self.players = [player1, player2]
        self.current = 0
        self.target = target
        self.die = Die(seed=seed)

    def _roll_die(self) -> int:
        return self.die.roll()

    def _switch(self):
        self.current = 1 - self.current

    def play(self):
        """Run the full game loop."""
        while all(p.score < self.target for p in self.players):
            player = self.players[self.current]
            turn_total = 0
            print(f"\n{player.name}'s turn (score: {player.score})")

            while True:
                decision = player.decide(turn_total)
                if decision == "roll":
                    roll = self._roll_die()
                    print(f"{player.name} rolled a {roll}")
                    if roll == 1:
                        print(f"{player.name} loses all points this turn.")
                        turn_total = 0
                        break
                    turn_total += roll
                    print(f"Turn total: {turn_total}")
                else:  # hold
                    player.score += turn_total
                    print(f"{player.name} holds. Total score: {player.score}")
                    break

            if player.score >= self.target:
                print(f"\n🏆 {player.name} wins with {player.score} points!")
                return player
            self._switch()
