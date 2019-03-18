import pygame
from starting_screen import *

mode = "STARTING SCREEN"
pygame.init()
DISPLAY = pygame.display.set_mode((1920, 1080))

screen1 = starting_screen()

screen1.draw(DISPLAY)

    
