import time
from piggame.timed_proxy import TimedGameProxy
from piggame.game import Game
from piggame.player import Player

class AlwaysRoll(Player):
    def decide(self, turn_total): 
        return "roll"

def test_proxy_returns_leader_when_time_expires():
    p1, p2 = AlwaysRoll("P1"), AlwaysRoll("P2")
    p1.score, p2.score = 30, 20  # P1 is ahead
    g = Game(p1, p2)
    proxy = TimedGameProxy(g, limit_seconds=0.0)  # expires immediately

    start = time.time()
    winner = proxy.play()
    end = time.time()

    assert winner is p1
    assert end - start < 1  # returned almost instantly
