import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, sj_game):
        super().__init__()
        self.screen = sj_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = sj_game.settings

        self.image= pygame.image.load("Small_tank.png")
        self.rect = self.image.get_rect()

        self.rect.x = (self.settings.tank_horizontal_space)*self.rect.width
        self.rect.y = (self.settings.tank_vertical_space)*self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.x += self.settings.tank_speed * self.settings.squadron_flank
        self.rect.x = self.x

    def check_edges(self):
        return (self.rect.right >= self.screen_rect.right) or self.rect.left<=0
