from pygame import font

class ScoreBoard:
    """A class for showing results in an accessible form."""
    def __init__(self, game):
        """Initialize the basic settings for the strings."""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.stats = game.stats

        self.text_color = (70, 70, 70)
        self.font = font.Font(None, 48)

        self.prep_all()

    def prep_all(self):
        """Prepare all images."""
        self.prep_level()
        self.prep_bullets_left()
        self.prep_score()
        self.prep_high_score()

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

    def prep_score(self):
        """Generates a image representig score."""
        score_str = str(round(self.stats.score, -1))
        self.score_img = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_img.get_rect()

        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.y = 10

    def prep_high_score(self):
        """Generates a image representig high score."""
        high_score_str = str(round(self.stats.high_score, -1))
        self.high_score_img = self.font.render(high_score_str, True, self.text_color)
        self.high_score_rect = self.high_score_img.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.y = 10

    def draw(self):
        """Draw the images, scores on the screen."""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.bullets_img, self.bullets_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
