class Settings:
    """An excelent and neat class to store all settings for Santa Jabalina"""

    def __init__(self):
        """Store all the games settings"""

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)
        self.fps = 60

        # Avatar settings
        self.avatar_speed = 10
        self.lives = 2

        # Bullet settings
        self.allowed_bullets = 4
        self.bullet_speed = 15
        self.bullet_width = 18
        self.bullet_height = 30
        self.bullet_color = (25, 234, 25)

        # Tank settings
        self.squadron_flank = 1
        self.tank_speed = 4
        self.tank_forward_speed = 0.1
        self.tank_horizontal_space = 0.8
        self.tank_vertical_space = 0.5
