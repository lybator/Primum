import sys
import time

import Map

"""from Actions import Create as cre
from Building import *"""
from Map import *
import os

TurnTimer = 0

player_map = map(10,10)
print(player_map.draw_matrix(player_map.draw_map()))
"""while(1):
    os.system('cls')
    print("The turn is {}".format(TurnTimer))
    print(player.buildQ())
    print("Current resources:\n"
          "Silver: {0}".format(player.silver))
    player.turn_resource_gathering()
    playerIn = input("What would you like to create master?:\n1) Barracks\n2) Supply\n3) Check Build Queue"
                     "\n4) Pass\n5) Soldier\n6) Dominion\n\n0) Exit\n")
    if int(playerIn) == 0:
        sys.exit()

    if int(playerIn) == 1:
        print(player.create_baracks())
        pass

    if int(playerIn) == 2:
        print(player.create_supply())
        pass

    if int(playerIn) == 3:
        print(player.buildQueue)
        pass

    if int(playerIn) == 4:
        continue

    if int(playerIn) == 5:
        print(player.create_soldier())

    if int(playerIn) == 6:
        print(player.D_names)

    playerIn = input("Your next action will end turn.")
    TurnTimer += 1
    os.system('cls')


"""