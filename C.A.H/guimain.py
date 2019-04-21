import pygame
from starting_screen import *
from settings_screen import *
from card_czar_screen import *
from players import *
from cards import *
pygame.init()
DISPLAY = pygame.display.set_mode((1920, 1080))

#SCREENS
starting = starting_screen()
settings = settings_screen()
who_czar = card_czar_screen()

#GAME START
starting.draw(DISPLAY)
settings.draw(DISPLAY)

#creating players...
PlayerNames = []
temp = settings.player_names.split(",")
for n in temp:
    PlayerNames.append(n.strip())

PLAYERS = [PLAYER(n) for n in PlayerNames]

#creating bot players...
for n in range(settings.number_of_bots):
    name = "BOT" + str(n)
    PLAYERS.append(PLAYER(name))

#assign each player 7 cards...
for n in range(len(PLAYERS)):
    for s in range(7):
        PLAYERS[n].assign_cards(WHITE.pop(random.randint(0,(len(WHITE)-1))))     #Gives each player random cards

turn = 0
won = False

while not won:
    if turn >= len(PLAYERS):
        turn = 0
    PLAYERS[turn].toggle_card_czar()
    who_czar.draw(DISPLAY, PLAYERS[turn].name)







    PLAYERS[turn].toggle_card_czar()
    turn += 1
