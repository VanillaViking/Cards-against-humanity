import pygame
from starting_screen import *
from settings_screen import *
pygame.init()
DISPLAY = pygame.display.set_mode((1920, 1080))

SCREENS = []
SCREENS.append(starting_screen())
SCREENS.append(settings_screen())

for n in SCREENS:
    n.draw(DISPLAY)