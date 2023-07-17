class GameStats:

    def __init__(self, sj_game):
        self.settings = sj_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.avatars_left = self.settings.lives