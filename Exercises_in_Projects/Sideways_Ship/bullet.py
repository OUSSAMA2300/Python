import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)

        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right

        self.x = float(self.rect.x)
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed

    def update(self):
        """Move the bullet up the  screen"""
        # Update the decimal vlaue of the bullet
        self.x += self.speed
        # Update the rect poistion
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)