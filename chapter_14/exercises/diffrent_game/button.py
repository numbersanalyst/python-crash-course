import pygame.font


class Button():
    """Button for the game with text."""

    def __init__(self, game, text):
        """Initialize the button."""

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.color = (255, 255, 255)
        self.bg_color = (25, 25, 25)
        self.width, self.height = 200, 85
        self.font = pygame.font.SysFont(None, 40)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_text = self._prep_text(text)

    def _prep_text(self, text):
        """Generetes and adds text to the button."""
        self.text = self.font.render(text, True, self.color)
        self.text_rect = self.text.get_rect()

        self.text_rect.center = self.rect.center

    def draw(self):
        """Draws the button on the screen."""
        self.screen.fill(self.bg_color, self.rect)  # fill the rect
        self.screen.blit(self.text, self.text_rect)  # add image (text)
