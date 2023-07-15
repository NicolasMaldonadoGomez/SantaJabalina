class Settings:
    """An excelent and neat class to store all settings for Santa Jabalina"""

    def __init__(self):
        """Store all the games settings"""

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (25,25,70)
        self.fps = 60

        # Ship settings
        self.ship_speed = 10