import sys
import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_event(event, ship)

def keydown_event(event, settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)

def keyup_event(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    if len(bullets) < settings.bullet_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= 1080:
            bullets.remove(bullet)
