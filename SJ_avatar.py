import pygame


class SJ_avatar:
    """This is the class that draws and controls motion of the player on screen"""

    def __init__(self, sj_game) -> None:
        """Initialize the avatar and draws it to position"""
        self.screen = sj_game.screen
        self.screen_rect = sj_game.screen.get_rect()
        self.settings = sj_game.settings
        # Load avatar image and its rect
        self.image = pygame.image.load("Santa_Jabalina.png")
        self.rect = self.image.get_rect()
        # Starts avatar at bottom center of screen
        self._center_avatar()
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_left and self.rect.left > -100:
            self.x -= self.settings.avatar_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.avatar_speed
        self.rect.x = self.x

    def _center_avatar(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blit_me(self):
        """blit is like draw on in games, so it draws the avatar at location"""
        self.screen.blit(self.image, self.rect)
