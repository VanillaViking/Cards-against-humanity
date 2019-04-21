import pygame
from button import *

class player_choose():
    def __init__(self):
        self.bgcolour = (240,240,240)

    def draw(self, DISPLAY, player_cards, black_card):
        black_button = button((0,0,0), 300, 400, ((1920/2) - 150, 200), black_card, (255,255,255), 20,28, False)
        button_pressed = False
        card_buttons = []
        x_pos = 50
        for cards in player_cards:
            card_buttons.append(button((255,255,255), 200, 300, (x_pos,800), cards, (0,0,0), 15, 28, False))
            x_pos += 250
        
        while not button_pressed:
            pygame.display.update()
            DISPLAY.fill(self.bgcolour)
            black_button.draw_button(DISPLAY)
            for n in card_buttons:
                n.draw_button(DISPLAY)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.QUIT
                    quit()
