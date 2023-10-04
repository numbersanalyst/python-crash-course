class Settings:
    """Settings for the Shotting Rocket game."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (255, 255, 255)
        # Rocket settings
        self.rocket_speed = 1.5
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_color = (60, 60, 60)
        self.bullet_width = 45
        self.bullet_height = 15
