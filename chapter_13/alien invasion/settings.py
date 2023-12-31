class Settings:
    """Class designed for storage all game settings."""

    def __init__(self) -> None:
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Aliens settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # Value fleet_direction 1 means right, 0 means left
        self.fleet_direction = 1