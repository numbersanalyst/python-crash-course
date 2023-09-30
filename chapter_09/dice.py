from random import randint


class Die():
    """A class representing an die throw."""

    def __init__(self, num_of_sides=6):
        """A die constructor."""
        self.sides = num_of_sides
        print(f'\n\tA die with {num_of_sides} sides has created.')

    def roll(self):
        """Simulate a die roll."""
        print('\nRolling...')
        number = randint(1, self.sides)
        print(f'The drawn number is {number}.')


die1 = Die()
for i in range(10):
    die1.roll()

die2 = Die(10)
for i in range(10):
    die2.roll()

die3 = Die(20)
for i in range(10):
    die3.roll()
