import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from audio import SoundPad
from button import Button
from ship import Ship
from alien import Alien
from bullet import Bullet


class AlienInvasion:
    """A general class designed to manage resources and how the game works."""

    def __init__(self):
        """Initialize the game and create their resorces."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.soundPad = SoundPad()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, 'Play')
        self._generate_difficulty_buttons()

    def run_game(self):
        """Run the main game loop."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _generate_difficulty_buttons(self):
        """Add buttons that allow to change the difficulty level."""
        self.easy_button = Button(self, 'Easy')
        self.medium_button = Button(self, 'Medium')
        self.hard_button = Button(self, 'Hard')

        # Set the positions of the buttons
        self._set_difficulty_buttons_y_position(10)

    def _set_difficulty_buttons_y_position(self, margin):
        """Set the horizontal position of the difficulty buttons."""
        self.easy_button.rect.top = self.play_button.rect.bottom + margin
        self.medium_button.rect.top = self.easy_button.rect.bottom + margin
        self.hard_button.rect.top = self.medium_button.rect.bottom + margin
        self._update_difficulty_buttons_text_position()

    def _reset_difficulty_buttons_x_position(self):
        """Reset the vertical position of the difficulty buttons."""
        self.easy_button.rect.x = self.play_button.rect.x
        self.medium_button.rect.x = self.easy_button.rect.x
        self.hard_button.rect.x = self.medium_button.rect.x
        self._update_difficulty_buttons_text_position()

    def _update_difficulty_buttons_text_position(self):
        """Set the text position correct on difficulty buttons."""
        self.easy_button.update_text_position()
        self.medium_button.update_text_position()
        self.hard_button.update_text_position()

    def _exit_game(self):
        """Save the progress and exit the game."""
        self.stats.save_high_score()
        sys.exit()

    def _check_events(self):
        """Reactions to events generated by mouse or keyboard."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._exit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                self._check_difficulty_buttons(mouse_pos)

    def _check_keydown_events(self, event):
        """Reactions to keydown events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reactions to keyup events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            self._exit_game()
        elif event.key == pygame.K_g:
            self._start_game()

    def _check_play_button(self, mouse_pos):
        """Try to start the game if play button is pressed."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self._start_game()
            self.soundPad.play('click')

    def _check_difficulty_buttons(self, mouse_pos):
        """If difficulty buttons are pressed change the level of difficulty."""
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)

        if easy_button_clicked or medium_button_clicked or hard_button_clicked:
            self._reset_difficulty_buttons_x_position()
            self.soundPad.play('click')

        if easy_button_clicked:
            self.settings.difficulty_level = 'easy'
            self.easy_button.rect.x += 10
            self.easy_button.update_text_position()
        elif medium_button_clicked:
            self.settings.difficulty_level = 'medium'
            self.medium_button.rect.x += 10
            self.medium_button.update_text_position()
        elif hard_button_clicked:
            self.settings.difficulty_level = 'difficult'
            self.hard_button.rect.x += 10
            self.hard_button.update_text_position()

    def _start_game(self):
        """Starts the game if the game is not already running."""
        if not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_images()
            self.stats.game_active = True

            self._reset_ship_bullets_aliens()

            pygame.mouse.set_visible(False)

    def _reset_ship_bullets_aliens(self):
        """Reset the ship, bullets and aliens position."""
        self.aliens.empty()
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.soundPad.play('fire')

    def _update_bullets(self):
        """Update the bullets positions and remove useless bullets."""
        # Update bullets positions.
        self.bullets.update()

        # Remove useless bullets located outside the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Reaction to collision between bullet and alien."""
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            self.soundPad.play('hit')

        if not self.aliens:
            self.start_new_level()

    def start_new_level(self):
        """Clear game and start a new level."""
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        self.stats.level += 1
        self.sb.prep_level()
        self.soundPad.play('lvl_up')


    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height

        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = self.settings.screen_height - \
            (3 * alien_height) - ship_height

        number_aliens_x = available_space_x // (2 * alien_width)
        number_rows = available_space_y // (2 * alien_height)

        # Create first row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create alien and add it to the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x

        alien.rect.y = alien_height + 2 * alien_height * row_number

        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Response when the alien will reach the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move all the fleet to the down and changes the direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Reaction to alien hit the ship."""
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.sb.prep_ships()

            self._reset_ship_bullets_aliens()
            self.soundPad.play('minus_life')

            sleep(0.5)
        else:
            self.soundPad.play('end')
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if the alien reaches the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        """Update the aliens positions."""
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _update_screen(self):
        """Update the images on the screen and move to new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
