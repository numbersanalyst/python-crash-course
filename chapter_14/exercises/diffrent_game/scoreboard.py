from pygame import font


class ScoreBoard:
    """A class for showing results in an accessible form."""

    def __init__(self, game):
        """Initialize the basic settings for the strings."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.stats = game.stats

        self.text_color = (70, 70, 70)
        self.label_color = (160, 160, 160)
        self.font = font.Font(None, 48)
        self.label_font = font.Font(None, 24)

        self.prep_all()

    def prep_all(self):
        """Prepare all images."""
        self.prep_level()
        self.prep_bullets_left()
        self.prep_score()
        self.prep_high_score()
        self.prep_labels()

    def prep_level(self):
        """Generates a image representig current game level."""
        level_str = str(self.stats.level)
        self.level_img = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_img.get_rect()

        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.y = 10

    def prep_bullets_left(self):
        """Generates a image representig bullets."""
        bullets_str = str(self.stats.bullets_left)
        self.bullets_img = self.font.render(bullets_str, True, self.text_color)
        self.bullets_rect = self.bullets_img.get_rect()

        self.bullets_rect.left = self.screen_rect.left + 20
        self.bullets_rect.y = 60

    def prep_high_score(self):
        """Generates a image representig high score."""
        high_score_str = str(round(self.stats.high_score, -1))
        self.high_score_img = self.font.render(
            high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_img.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.y = 10

    def prep_score(self):
        """Generates a image representig score."""
        score_str = str(round(self.stats.score, -1))
        self.score_img = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_img.get_rect()

        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.y = 10

    def prep_labels(self):
        """Add labels to existing values ​​that are on the screen."""
        self.level_label_img = self.label_font.render(
            'Level', True, self.label_color)
        self.bullets_label_img = self.label_font.render(
            'Bullets left', True, self.label_color)
        self.high_score_label_img = self.label_font.render(
            'High Score', True, self.label_color)
        self.score_label_img = self.label_font.render(
            'Score', True, self.label_color)

        # Init the positions
        self.level_label_rect = self.level_label_img.get_rect()
        self.bullets_label_rect = self.bullets_label_img.get_rect()
        self.high_score_label_rect = self.high_score_label_img.get_rect()
        self.score_label_rect = self.score_label_img.get_rect()

        # Set the positions
        self.level_label_rect.top = self.level_rect.bottom
        self.level_label_rect.left = self.level_rect.left

        self.bullets_label_rect.top = self.bullets_rect.bottom
        self.bullets_label_rect.left = self.bullets_rect.left

        self.high_score_label_rect.top = self.high_score_rect.bottom
        self.high_score_label_rect.centerx = self.high_score_rect.centerx

        self.score_label_rect.top = self.score_rect.bottom
        self.score_label_rect.right = self.score_rect.right

    def draw(self):
        """Draw the images, scores on the screen."""
        self.screen.blit(self.level_img, self.level_rect)
        self.screen.blit(self.bullets_img, self.bullets_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.score_img, self.score_rect)

    def draw_labels(self):
        """Draw the labels for the images and scores on the screen."""
        self.screen.blit(self.level_label_img, self.level_label_rect)
        self.screen.blit(self.bullets_label_img, self.bullets_label_rect)
        self.screen.blit(self.high_score_label_img, self.high_score_label_rect)
        self.screen.blit(self.score_label_img, self.score_label_rect)