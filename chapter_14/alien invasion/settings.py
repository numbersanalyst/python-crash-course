class Settings:
    """Class designed for storage all game settings."""

    def __init__(self) -> None:
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Aliens settings
        self.fleet_drop_speed = 10

        # Easy change speed game
        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.difficulty_level = 'medium'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that will be change trough the game."""
        if self.difficulty_level == 'easy':
            self.ship_speed = 1.5
            self.bullet_speed = 2.0
            self.alien_speed = 0.8
            self.bullets_allowed = 5
            self.ship_limit = 3
            self.alien_points = 50
        elif self.difficulty_level == 'medium':
            self.ship_speed = 1.5
            self.bullet_speed = 3.0
            self.alien_speed = 1.0
            self.bullets_allowed = 3
            self.ship_limit = 2
            self.alien_points = 35
        elif self.difficulty_level == 'difficult':
            self.ship_speed = 2.5
            self.bullet_speed = 2.5
            self.alien_speed = 1.2
            self.bullets_allowed = 2
            self.ship_limit = 1
            self.alien_points = 10

        # Value fleet_direction 1 means right, 0 means left
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)