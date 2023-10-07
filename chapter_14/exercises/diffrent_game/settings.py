class Settings:
    """Settings for the game."""

    def __init__(self):
        """Initialize the settings data."""
        # Window settings
        self.w_width = 1000
        self.w_height = 800
        self.background = (250, 250, 250)
        # Ship settings
        self.s_speed = 1.1
        self.s_ammo = 3
        # Bullet settings
        self.b_color = (0,0,0)
        self.b_width = 25
        self.b_height = 5
        self.b_speed = 2.5
        # Rect settings
        self.r_width = 40
        self.r_height = 65
        self.r_color = (0, 0, 0)
        self.r_speed = 0.5
