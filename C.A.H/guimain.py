import pygame
from starting_screen import *
from settings_screen import *
from card_czar_screen import *
from whos_turn_screen import *
from player_choose import *
from players import *
from cards import *
pygame.init()
DISPLAY = pygame.display.set_mode((1920, 1080))

#SCREENS
starting = starting_screen()
settings = settings_screen()
who_czar = card_czar_screen()
which_player =  player_turn()
player_choose = player_choose()

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
    who_czar.draw(DISPLAY, PLAYERS[turn].name)          #show card czar

    black_card = BLACK[random.randint(0,len(BLACK)-1)]      #select random black card

    #show which player's turn
    for n in range(len(PLAYERS)):
        if not PLAYERS[n].is_card_czar and "BOT" not in PLAYERS[n].name:
            which_player.draw(DISPLAY, PLAYERS[n].name)
            player_choose.draw(DISPLAY, PLAYERS[n].cards, black_card)










    PLAYERS[turn].toggle_card_czar()
    turn += 1
