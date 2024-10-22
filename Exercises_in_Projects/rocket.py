import pygame

class Rocket():

    def __init__(self, setting, screen):
        self.screen = screen
        self.setting = setting

        self.org_image = pygame.image.load('images/MilitaryRocketWithFlames_0.png')
        self.image = pygame.transform.scale(self.org_image, (200, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on movement flags"""
        # Horizontal movement
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.setting.speed
        elif self.moving_left and self.rect.left > 0:
            self.centerx -= self.setting.speed 

        # Vertical movement
        elif self.moving_up and self.rect.top > 0:
            self.centery -= self.setting.speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.setting.speed

        # Update rect object from self.centerx and self.centery
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)