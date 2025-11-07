from piggame.factory import PlayerFactory
from piggame.player import HumanPlayer
from piggame.computer_player import ComputerPlayer
import pytest

def test_factory_creates_human_and_computer():
    human = PlayerFactory.create("human", "Alice")
    comp = PlayerFactory.create("computer", "CPU")

    assert isinstance(human, HumanPlayer)
    assert isinstance(comp, ComputerPlayer)

def test_factory_rejects_unknown_type():
    with pytest.raises(ValueError):
        PlayerFactory.create("alien", "E.T.")
