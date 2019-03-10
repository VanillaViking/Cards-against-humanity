import pygame

class starting_screen():
    def __init__(self):
        self.bgcolour = (255,255,255)
    
    def draw(self, DISPLAY):
        pygame.display.update()
        DISPLAY.fill(self.bgcolour)