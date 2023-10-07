import pygame


class Bullet(pygame.sprite.Sprite):
    """A class representing a bullet object."""

    def __init__(self, game):
        """Initialize the Bullet object :)"""
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.ship_rect = game.ship.rect

        self.rect = pygame.Rect(0, 0, self.settings.b_width, self.settings.b_height)
        self.rect.midleft = self.ship_rect.midright

        self.x = float(self.rect.x)

    def update(self):
        """Change the position of the bullet."""
        self.x += self.settings.b_speed
        self.rect.x = self.x

    def draw(self):
        """Draw the bullet on the screen."""
        pygame.draw.rect(self.screen, self.settings.b_color, self.rect)