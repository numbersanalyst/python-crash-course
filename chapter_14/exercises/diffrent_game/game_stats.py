class GameStats:
    """Stroing data about the game status."""

    def __init__(self, game):
        """Initialize statistics data."""
        self.settings = game.settings
        self.game_active = False
        self.reset()

    def reset(self):
        """Initializate and reset the game stats."""
        self.bullets_left = self.settings.s_ammo
