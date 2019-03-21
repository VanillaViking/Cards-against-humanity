import pygame
pygame.font.init()
arial = pygame.font.SysFont('Arial', 30)

class button():
    def __init__(self, colour, width, length, pos, text=''):
        self.colour = colour
        self.length = length
        self.width = width
        self.pos = pos
        self.text = arial.render(text, False, (0,0,0))
    def draw_button(self, DISPLAY):
        pygame.draw.rect(DISPLAY, self.colour, (self.pos[0], self.pos[1], self.width, self.length))
        DISPLAY.blit(self.text, (self.pos[0] + ((self.width/2) - (self.text.get_width()/2)), self.pos[1] + ((self.length/2) - (self.text.get_height() / 2))))
    
    def isOver(self, mouse_pos):
            if self.pos[0] < mouse_pos[0] and mouse_pos[0] < (self.pos[0] + self.width):
                if self.pos[1] < mouse_pos[1] and mouse_pos[1] < (self.pos[1] + self.length):
                    return True

            return False 