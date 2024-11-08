import pygame
from pygame.sprite import Group

from side_settings import Settings
import side_functions as sf
from sideway_ship import Ship



def run_side():

    pygame.init()

    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Sideways Ship")

    bullets = Group()

    ship = Ship(settings, screen)

    while True:

        sf.check_events(settings, screen, ship, bullets)       
        ship.update()
        bullets.update()
        sf.update_bullets(bullets)
        sf.update_screen(settings, screen, ship, bullets)

       

run_side()