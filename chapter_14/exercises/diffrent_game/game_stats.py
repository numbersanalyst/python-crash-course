import json


class GameStats:
    """Stroing data about the game status."""

    def __init__(self, game):
        """Initialize statistics data."""
        self.settings = game.settings
        self.game_active = False
        self.high_score = self.load_high_score()
        self.reset()
        self.reset_bullets()

    def reset(self):
        """Initializate and reset the game stats."""
        self.level = 1
        self.score = 0

    def reset_bullets(self):
        """Initializate and reset the stats about bullets."""
        self.bullets_left = self.settings.s_ammo

    def load_high_score(self):
        """Load the best score from file."""
        try:
            with open("record.json", "r") as f:
                return json.load(f)
        except:
            return 0

    def save_high_score(self):
        """Save the best score in file."""
        if self._check_stored_high_score():
            with open("record.json", "w") as f:
                json.dump(self.high_score, f)

    def _check_stored_high_score(self) -> bool:
        """Check if the current score is bigger than the stored score."""
        stored_score = self.load_high_score()
        if stored_score < self.high_score:
            return True
