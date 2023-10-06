import pygame

class Ship:
    """Class designed to control the spaceship."""

    def __init__(self, ai_game):
        """Initialize the spaceship and its launch position."""

        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship will appear on the bottom screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Ship verticall position converted to float.
        self.x = self.rect.x

        # Options to move the ship.
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the spaceship's position based on its movement option."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update position of the object rect based on the value of self.x.
        self.rect.x = self.x

    def blitme(self):
        """Display the spaceship at its actual position."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place the ship in the center of the bottom screen edge."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)