class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullets settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.buleet_color = 60, 60, 60