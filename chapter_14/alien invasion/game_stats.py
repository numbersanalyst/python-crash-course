import json


class GameStats:
    """Monitoring in-game statistical data"""

    def __init__(self, ai_game):
        """Initialize statistics data."""
        self.settings = ai_game.settings
        self.game_active = False
        self.high_score = self.load_high_score()
        self.reset_stats()

    def load_high_score(self) -> int:
        """Load the best score from file and return its."""
        try:
            with open("record.json") as f:
                return json.load(f)
        except FileNotFoundError:
            print("****File with record not found.")
            return 0
        except Exception as err:
            print(f"****Error: {err}.")
            return 0

    def _check_storage_high_score(self) -> bool:
        """Check if the current score is higher than the stored score."""
        saved_high_score = self.load_high_score()
        if saved_high_score < self.high_score:
            return True

    def save_high_score(self):
        """Save the best score in a file."""
        higher_score = self._check_storage_high_score()
        if higher_score:
            with open("record.json", "w") as f:
                json.dump(self.high_score, f)

    def reset_stats(self):
        """Initialize statistics data witch can change during game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
