import random

class Die:
    """A simple six-sided die."""

    def __init__(self, sides=6, seed=None):
        self.sides = sides
        if seed is not None:
            random.seed(seed)

    def roll(self) -> int:
        """Roll the die and return the value between 1 and sides."""
        return random.randint(1, self.sides)
