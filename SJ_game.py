import pygame
from sys import exit
from time import sleep

from SJ_settings import Settings
from game_stats import GameStats
from SJ_avatar import SJ_avatar
from SJ_bullet import Bullet
from SJ_tanks import Tank



class Santa_Jabalina_vs:
    """To manage behaviors and game assets"""

    def __init__(self):
        """Initialize the game and create resources"""
        pygame.init
        # pygame.display.set_caption("Santa Jabalina vs...")
        self.playing = True
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.avatar = SJ_avatar(self)
        self.bullets = pygame.sprite.Group()
        self.tanks = pygame.sprite.Group()
        self.stats = GameStats(self)
        self._create_squadron()

    def run_game(self):
        """Run the game, which is to start the game loop"""
        while True:
            self._check_events()
            if self.playing:
                self.avatar.update()
                self._update_tanks()
                self._update_bullets()
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """we listen for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.avatar.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.avatar.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.avatar.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.avatar.moving_left = False
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            exit()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.allowed_bullets:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.tanks.draw(self.screen)
        self.avatar.blit_me()
        pygame.display.flip()

    def _update_bullets(self):
        self._remove_out_of_sight_bullets()
        self.bullets.update()
        self._check_bullet_collisions()
    
    def _check_bullet_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.tanks, True, True)
        if not self.tanks:
            self.bullets.empty()
            self._create_squadron()

    def _remove_out_of_sight_bullets(self):
        for bullet in self.bullets.copy():
            # you can’t remove items from a list or group within a for loop, so we have to loop over a copy of the group
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_squadron(self):
        new_tank = Tank(self)
        tank_width = new_tank.rect.width
        tank_height = new_tank.rect.height

        number_of_tanks = int(
            self.settings.screen_width
            / (tank_width * (1 + self.settings.tank_horizontal_space))
        )
        first_tank_x = int(
            (
                self.settings.screen_width
                - number_of_tanks * tank_width
                - (number_of_tanks - 1)
                * tank_width
                * self.settings.tank_horizontal_space
            )
            / 2
        )

        number_of_rows = int(
            (self.settings.screen_height - self.avatar.rect.height)
            / (tank_height * (1 + self.settings.tank_vertical_space))
        )
        first_tank_y = int(
            (
                self.settings.screen_height
                - self.avatar.rect.height
                - number_of_rows * tank_height
                - (number_of_rows - 1) * tank_height * self.settings.tank_vertical_space
            )
            / 2
        )

        for i in range(number_of_rows):
            tank_y = first_tank_y + i * tank_height * (
                1 + self.settings.tank_vertical_space
            )
            self._create_line_of_tanks(number_of_tanks, first_tank_x, tank_y)

    def _create_line_of_tanks(self, number_of_tanks, first_tank_x, tank_y):
        current_x = first_tank_x
        for _ in range(number_of_tanks - 1):
            new_tank = Tank(self)
            new_tank.x = current_x
            new_tank.rect.x = current_x
            new_tank.rect.y = tank_y
            self.tanks.add(new_tank)
            current_x += (self.settings.tank_horizontal_space + 1) * new_tank.rect.width

    def _update_tanks(self):
        self._check_squadron_edge()
        self.tanks.update()
        self._check_tank_avatar_collision()
        self._check_tank_invasion()

    def _sj_down(self):
        if self.stats.avatars_left>0:
            self.stats.avatars_left -= 1
            self.bullets.empty()
            self.tanks.empty()
            self._create_squadron()
            self.avatar._center_avatar()
            print("Saint Javelins left:",self.stats.avatars_left)
        else:
            self.playing = False
            print("Paila, Game over, Insert Coin")
        sleep(0.5)

    def _check_tank_avatar_collision(self):
        if pygame.sprite.spritecollideany(self.avatar, self.tanks):
            self._sj_down()

    def _check_squadron_edge(self):
        for tank in self.tanks:
            if tank.check_edges():
                self._change_squadron_direction()
                break

    def _change_squadron_direction(self):
        for tank in self.tanks:
            tank.rect.y += self.settings.tank_forward_speed * tank.rect.height
        self.settings.squadron_flank *= -1

    def _check_tank_invasion(self):
        """Check if a tank hit the bottom of the screen"""
        for tank in self.tanks:
            if tank.rect.bottom >= self.settings.screen_height:
                self._sj_down()
                break

if __name__ == "__main__":
    # Start the game by intanciate a Santa Jabalina object

    sj = Santa_Jabalina_vs()
    sj.run_game()
