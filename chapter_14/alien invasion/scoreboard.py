import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """Class representing information about a score."""

    def __init__(self, ai_game):
        """Initialize the attributes regarding points."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.label_color = (90, 90, 90)
        self.font = pygame.font.SysFont(None, 48)
        self.label_font = pygame.font.SysFont(None, 24)

        self.prep_images()

    def prep_images(self):
        """Generate the images and give it a position."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_labels()

    def prep_score(self):
        """Transform the score to generated image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Transform the best score in the game to generated image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check if the record has been broken."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Transform the level to generated image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color)

        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_rect.right
        self.level_image_rect.top = self.score_rect.bottom + 15

    def prep_ships(self):
        """Displays the number of ships the player has left."""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_labels(self):
        """Add labels to existing values ​​that are on the screen."""
        self.ships_label = self.label_font.render(
            'Lives', True, self.label_color)
        self.high_score_label = self.label_font.render(
            'High Score', True, self.label_color)
        self.score_label = self.label_font.render(
            'Score', True, self.label_color)
        self.level_label = self.label_font.render(
            'Level', True, self.label_color)

        # Get the positions / rects
        self.ships_label_rect = self.ships_label.get_rect()
        ship = self.ships.sprites()[0]

        self.high_score_label_rect = self.high_score_label.get_rect()
        self.score_label_rect = self.score_label.get_rect()
        self.level_label_rect = self.level_label.get_rect()

        # Set the positions
        self.ships_label_rect.top = ship.rect.bottom
        self.ships_label_rect.centerx = ship.rect.centerx

        self.high_score_label_rect.x = self.high_score_rect.x
        self.high_score_label_rect.top = self.high_score_rect.bottom

        self.score_label_rect.right = self.score_rect.right
        self.score_label_rect.top = self.score_rect.bottom

        self.level_label_rect.right = self.level_image_rect.right
        self.level_label_rect.top = self.level_image_rect.bottom

    def show_score(self):
        """Show the score on the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        self.ships.draw(self.screen)

        self.show_labels()

    def show_labels(self):
        """Show the labels on the screen."""
        self.screen.blit(self.ships_label, self.ships_label_rect)
        self.screen.blit(self.high_score_label, self.high_score_label_rect)
        self.screen.blit(self.score_label, self.score_label_rect)
        self.screen.blit(self.level_label, self.level_label_rect)
