import pygame

class Ship():

    def __init__(self, setting, screen):
        self.screen = screen
        self.setting = setting

        self.org_image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.org_image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the left center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Store a decimal value for the ship's center.
        self.centery = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def update(self): 
        if self.moving_up and self.rect.top > 0: 
            self.centery -= self.setting.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.setting.speed

        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)