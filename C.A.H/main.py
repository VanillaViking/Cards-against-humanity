from cards import *
from players import *
import random
import os
player_picks = []
won = False
clear = lambda: os.system('clear')


playerNames = []
inp = input("Enter player name: ")
while inp:
        playerNames.append(inp)
        inp = input("Enter player name: ")      #Take the input of the names of all players and put it in a list
PLAYERS = [PLAYER(n) for n in playerNames]      # the list of all the player objects
while True:
        try:
                clear()
                winning_points = int(input("How many points to win?"))
                break
        except ValueError:
                input("Enter a number, buddy")

#RAndomly giving each player four cards. Also this could probably go in players.py, something to think about later
for n in range(len(PLAYERS)):
    for s in range(10):
        PLAYERS[n].assign_cards(WHITE.pop(random.randint(0,(len(WHITE)-1))))     #Gives each player four random cards
x = 0




while not won:
        black_card = BLACK[random.randint(0,len(BLACK)-1)]

        PLAYERS[x].toggle_card_czar()
        print( "\n----------------\n\n\n%s is the card czar\n\n\n----------------\n" % PLAYERS[x].name)
        input("Enter to continue")
        clear()

        for l in range(len(PLAYERS)):
                if not PLAYERS[l].is_card_czar:
                        clear()
                        input("%s's turn \n\n Enter to continue\n" % PLAYERS[l].name)
                        while True:
                                clear()
                                print("\n\n********************\n\n\n%s\n\n\n********************" % black_card)
                                for c,n in enumerate(PLAYERS[l].cards):
                                        print("%s: %s\n" % (c,n))
                                try:
                                        PLAYERS[l].choose()     #let player choose a card unless they are the card czar
                                        break
                                except ValueError:      #input Validation...
                                        clear()
                                        input("Enter a number, buddy")
                                except IndexError:
                                        clear()
                                        input("You don't have a card corresponding with that number.")

        for v in range(len(PLAYERS)):
                if PLAYERS[v].is_card_czar:
                        clear()
                        print("TIME FOR %s TO  JUDGE\n\n" % PLAYERS[v].name) 
                        input("Enter to continue")
                                
                        while True:
                                print(black_card, "\n\n")
                                for i in range(len(PLAYERS)):      #prints each person's chosen card for the judge to choose
                                        if not PLAYERS[i].is_card_czar:
                                                print(PLAYERS[i].chosen_card, "\n")
                                                player_picks.append(PLAYERS[i].chosen_card)
                                try:        
                                        winner_card = int(input("choose a card: "))
                                        for u in range(len(PLAYERS)):
                                                if not PLAYERS[i].is_card_czar:
                                                        if player_picks[winner_card-1] == PLAYERS[u].chosen_card:     #identifies who the chosen card belongs to
                                                                clear()
                                                                print("%s got a point!" % PLAYERS[u].name)
                                                                PLAYERS[u].give_point()
                                                                input("Enter to continue:")
                                                                clear()
                                                                if PLAYERS[u].points >= winning_points: #checking if player has won
                                                                        winner = PLAYERS[u].name 
                                                                        won = True
                                        break
                                except ValueError:      #input Validation...
                                        clear()
                                        input("Enter a number, buddy")
                                        clear()
                                except IndexError:
                                        clear()
                                        input("Try Again\nEnter to continue")
                                        clear()
                                
        for t in range(len(PLAYERS)):
                PLAYERS[t].clear_choice()       #clears everyones choices
                PLAYERS[t].get_card()

        player_picks = []                       #clears the chosen cards

        PLAYERS[x].toggle_card_czar()   #toggle card czar since their turn is done
        x += 1
        if x >= len(PLAYERS):
                x = 0

        

print("Looks like %s went SICKO MODE!" % winner)
input("Enter to continue")









