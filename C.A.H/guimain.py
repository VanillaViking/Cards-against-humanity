import pygame
from starting_screen import *
from settings_screen import *

mode = "STARTING SCREEN"
pygame.init()
DISPLAY = pygame.display.set_mode((1920, 1080))

screen1 = starting_screen()
screen2 = settings_screen()

screen1.draw(DISPLAY)
screen2.draw(DISPLAY)

    
