import pygame


class Bullet(pygame.sprite.Sprite):
    """A class to manage bullets"""

    def __init__(self, sj_game):
        super().__init__()
        self.screen = sj_game.screen
        self.settings = sj_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = sj_game.avatar.rect.midtop
        self.rect.x += 50
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
