import pygame


class Bullet(pygame.sprite.Sprite):
    """Class designed to control and create bullets."""

    def __init__(self, sr_game):
        """Initialize the bullet at the rocket position."""
        super().__init__()
        self.screen = sr_game.screen
        self.settings = sr_game.settings

        self.color = self.settings.bullet_color
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        self.speed = self.settings.bullet_speed

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midleft = sr_game.rocket.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Update the position of the bullet."""
        self.x += self.speed
        self.rect.x = self.x

    def draw(self):
        """Display the bullet at the specified position."""
        pygame.draw.rect(self.screen, self.color, self.rect)
