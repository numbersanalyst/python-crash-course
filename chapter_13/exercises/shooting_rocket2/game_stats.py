class GameStats:
    """Storage the game stats."""

    def __init__(self, game):
        self.settings = game.settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """Reset the game stats."""
        self.rocket_lives = self.settings.rocket_limit
