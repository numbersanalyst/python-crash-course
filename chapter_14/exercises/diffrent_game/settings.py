class Settings:
    """Settings for the game."""

    def __init__(self):
        """Initialize the settings data."""
        # Window settings
        self.w_width = 1000
        self.w_height = 800
        self.background = (250, 250, 250)
        # Ship settings
        self.s_ammo = 3
        # Bullet settings
        self.b_color = (0, 0, 0)
        self.b_width = 25
        self.b_height = 5
        # Rect settings
        self.r_width = 40
        self.r_height = 65
        self.r_color = (0, 0, 0)

        self.hit_points = 50
        self.score_scale = 1.5

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that will be change trought the game."""
        self.s_speed = 1.0
        self.b_speed = 1.5
        self.r_speed = 0.4
        self.hit_point = 50

    def increase_speed(self):
        """Incrase the speed settings. Game will be faster and you will recive more points."""
        self.s_speed *= self.speedup_scale
        self.b_speed *= self.speedup_scale
        self.r_speed *= self.speedup_scale
        self.hit_points = int(self.hit_points * self.score_scale)
