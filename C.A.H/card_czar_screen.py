import pygame
from button import *
pygame.font.init()
class card_czar_screen():
    def __init__(self):
        self.button_pressed = False
    
    def draw(self, DISPLAY, czar):
        self.button_pressed = False
        czar_text = arial.render(czar +" is the card czar.", True, (255,255,255))
        cont_button = button((255, 255, 255), 200, 75, ((1920/2) - 100, 800), "continue")

        while not self.button_pressed:
            pygame.display.update()
            DISPLAY.fill((0,0,0))
            DISPLAY.blit(czar_text, ((1920 / 2) - (czar_text.get_width() / 2),(200) - (czar_text.get_height() / 2)))
            cont_button.draw_button(DISPLAY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()

                if event.type == pygame.MOUSEMOTION:
                    if cont_button.isOver(pygame.mouse.get_pos()):
                        cont_button.colour = (200, 200, 200)
                    else:
                        cont_button.colour = (255, 255, 255)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cont_button.isOver(pygame.mouse.get_pos()):
                        self.button_pressed = True
