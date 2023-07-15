from SJ_avatar import SJ_avatar
from settings import Settings

import pygame
from sys import exit


class Santa_Jabalina_vs:
    """To manage behaviors and game assets"""

    def __init__(self) -> None:
        """Initialize the game and create resources"""
        pygame.init
        # pygame.display.set_caption("Santa Jabalina vs...")
        self.settings = Settings()
        self.screen   = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width= self.screen.get_rect().width
        self.settings.screen_height= self.screen.get_rect().height
        self.clock    = pygame.time.Clock()
        self.avatar   = SJ_avatar(self)

    def run_game(self):
        """Run the game, which is to start the game loop"""
        while True:
            self._check_events  (                 )
            self.avatar.update     (           )
            self._update_screen  (               )
            self.clock.tick     (self.settings.fps)
    
    def _check_events(self):
        """ we listen for keyboard and mouse events"""
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

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.avatar.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.avatar.moving_left = False
        elif event.key == pygame.K_q:
            exit()

    
    def _update_screen   (self):
        self.screen.fill   (self.settings.bg_color)
        self.avatar.blit_me  (    )
        pygame.display.flip   (    )


if __name__ == "__main__":
    # Start the game by intanciate a Santa Jabalina object

    sj = Santa_Jabalina_vs()
    sj.run_game()
