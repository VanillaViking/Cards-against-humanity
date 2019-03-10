import pygame
from starting_screen import *

mode = "STARTING SCREEN"
pygame.init()
DISPLAY = pygame.display.set_mode((1920, 1080))

screen1 = starting_screen()

while True:      #Game loop
    if mode == "STARTING SCREEN":
        screen1.draw(DISPLAY)