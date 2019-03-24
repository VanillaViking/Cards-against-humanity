import pygame
from button import *
from text_input import *

pygame.font.init()
class settings_screen():
    def __init__(self):
        self.bg_colour = (255,255,255)
        self.button_pressed = False
        self.text1 = FONT.render("Max points to win:",True, (200,200,200))
    
    def draw(self, DISPLAY):
        max_points = text_input(DISPLAY, (1920/2)-100, 200, 200, 75)
        while not self.button_pressed:      #game loop
            pygame.display.update() 
            DISPLAY.fill(self.bg_colour)
            DISPLAY.blit(self.text1,((1920/2)-(self.text1.get_rect().width/2),160))
            max_points.draw()

            for event in pygame.event.get():
              max_points.activate(event)
              if event.type == pygame.QUIT:
                  self.button_pressed = True