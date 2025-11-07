import time

class TimedGameProxy:
    """Proxy around Game that enforces a time limit and returns the leader if time expires."""

    def __init__(self, real_game, limit_seconds: float = 60.0):
        self._g = real_game
        self._limit = limit_seconds

    def play(self):
        start = time.time()
        while all(p.score < self._g.target for p in self._g.players):
            if time.time() - start >= self._limit:
                print("\n⏰ Time's up! Selecting current leader...")
                return max(self._g.players, key=lambda p: p.score)

            player = self._g.players[self._g.current]
            turn_total = 0
            while True:
                if time.time() - start >= self._limit:
                    print("\n⏰ Time's up! Selecting current leader...")
                    return max(self._g.players, key=lambda p: p.score)
                decision = player.decide(turn_total)
                if decision == "roll":
                    roll = self._g._roll_die()
                    if roll == 1:
                        turn_total = 0
                        break
                    turn_total += roll
                else:
                    player.score += turn_total
                    break

            if player.score >= self._g.target:
                print(f"\n🏆 {player.name} wins with {player.score} points!")
                return player
            self._g._switch()
