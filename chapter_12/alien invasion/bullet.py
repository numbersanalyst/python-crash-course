import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class designed to control bullets fired by a ship."""

    def __init__(self, ai_game):
        """Initialize a new Bullet object at the ship position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Create a bullet rectangle at position 0,0
        # and then define the corresponding position for it.
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
                                 self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet position is defined by float value.
        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet on the screen."""
        # Update the bullet position.
        self.y -= self.settings.bullet_speed
        # Update the bullet rectangle position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Displays the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)