from piggame.computer_player import ComputerPlayer

def test_computer_player_strategy_thresholds():
    cpu = ComputerPlayer("CPU")

    cpu.score = 70  # hold_at = min(25, 100 - 70) = 25
    assert cpu.decide(24) == "roll"
    assert cpu.decide(25) == "hold"

    cpu.score = 90  # hold_at = min(25, 10) = 10
    assert cpu.decide(9) == "roll"
    assert cpu.decide(10) == "hold"
