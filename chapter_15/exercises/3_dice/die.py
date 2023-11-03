from random import randint


class Die:
    """Class representing the single die for a game."""

    def __init__(self, num_sides=6):
        """Initialize the size of the die."""
        self.num_sides = num_sides

    def roll(self):
        """Returns the number from 1 to number of sides."""
        return randint(1, self.num_sides)
