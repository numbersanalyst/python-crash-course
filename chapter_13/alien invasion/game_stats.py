class GameStats:
    """Monitoring in-game statistical data"""

    def __init__(self, ai_game):
        """Initialize statistics data."""
        self.settings = ai_game.settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics data witch can change during game."""
        self.ship_left = self.settings.ship_limit