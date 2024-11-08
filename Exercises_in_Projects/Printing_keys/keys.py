# 12-4
import pygame

import sys

def run_keys():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Keys events")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(f"Key pressed: {pygame.key.name(event.key)}")


        bg = (255, 255, 255)

        screen.fill(bg)
        pygame.display.flip()
    

run_keys()