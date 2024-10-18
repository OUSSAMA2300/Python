import pygame

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen 

        # Load the ship image to and get its starting position
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.bottom
        self.rect.bottom = self.screen_rect.botoom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)