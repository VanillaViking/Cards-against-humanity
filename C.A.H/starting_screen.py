import pygame
from button import *

pygame.font.init()
arial = pygame.font.SysFont('Arial', 69)
cont_button = button((255, 255, 255), 200, 75, ((1920/2) - 100, 800), "continue")
class starting_screen():
    def __init__(self):
        self.bgcolour = (0,0,0)
        self.buttonPressed = False
        self.text = arial.render("Cards Against Humanity", True,(255,255,255))
    
    def draw(self, DISPLAY):
        while not self.buttonPressed: #game loop
            pygame.display.update()
            DISPLAY.fill(self.bgcolour)
            DISPLAY.blit(self.text, ((1920 / 2) - (self.text.get_width() / 2),(200) - (self.text.get_height() / 2)))
            cont_button.draw_button(DISPLAY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()