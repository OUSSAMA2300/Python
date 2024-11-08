import pygame

from settings import Settings
from rocket import Rocket
import functions as f

def run_game():

    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode(
        (setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Rocket")

    rocket = Rocket(setting, screen)

    while True:

        
        f.check_events(rocket)
        rocket.update()

        
        screen.fill(setting.bg_color)
        rocket.blitme()

        pygame.display.flip()

run_game()