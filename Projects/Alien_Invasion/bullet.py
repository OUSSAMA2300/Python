import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Creat a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                        ai_settings.bullet_height)
        
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's postion as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed
    def update(self):
        """Move the bullet up the  screen"""
        # Update the decimal vlaue of the bullet
        self.y -= self.speed
        # Update the rect poistion
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)