import pygame

class SJ_avatar:
    """This is the class that draws and controls motion of the player on screen"""

    def __init__(self, sj_game) -> None:
        """Initialize the avatar and draws it to position"""
        self.screen      = sj_game.screen
        self.screen_rect = sj_game.screen.get_rect()
        # Load avatar image and its rect
        self.image = pygame.image.load("Santa_Jabalina.png")
        self.rect  = self.image.get_rect()
        #Starts avatar at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_me(self):
        """blit is like draw on in games, so it draws the avatar at location"""
        self.screen.blit(self.image, self.rect)