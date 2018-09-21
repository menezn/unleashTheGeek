import sys
import math
import numpy
from random import randint

from functions import *
from entity import *
from utility import *

from roles import *
from board import *
from action import *

# Global Variables
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())
sqrtTwo = 2**.5

# game loop
while True:
    currentState = setUpBoard()
    print(str(currentState))#, file=sys.stderr)
    for i in range(heroes_per_player):
        moves = currentState.generateHeroMoves(i)
        print("Turns: " + str(len(moves)) + "\n")
        for move in moves:
            print("\t" + str(move))
        print("\n")
        print("WAIT")
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # if len(monsterData) == 0 and i != 2:
        #     #print("WAIT")
        #     if i == 0:
        #         print("MOVE", abs(base_x-800), abs(base_y-800))
        #         continue
        #     if i == 1:
        #         print("MOVE", abs(base_x-3500), abs(base_y-3500))
        #         #print("MOVE 1000 3500")
        #         continue
        # else:
        #     if (i != 2 and distance(base_x,base_y,heroData[i].x,heroData[i].y) > 7000):
        #         print("MOVE",base_x,base_y)
        #         continue
        #
        #     if (i == 0):
        #         selectedMonster = 0
        #         for j in range(len(monsterData)):
        #             if (10*(1/(distance(heroData[i].x,heroData[i].y,monsterData[j].x,monsterData[j].y)+1)) + 10000*(1/(distance(base_x,base_y,monsterData[j].x,monsterData[j].y)+1)) + 5000*monsterData[j].near_base) > (10*(1/(distance(heroData[i].x,heroData[i].y,monsterData[selectedMonster].x,monsterData[selectedMonster].y)+1)) + 10000*(1/(distance(base_x,base_y,monsterData[selectedMonster].x,monsterData[selectedMonster].y)+1)) + 5000*monsterData[selectedMonster].near_base):
        #                 selectedMonster = j
        #         if (distance(base_x,base_y,monsterData[selectedMonster].x,monsterData[selectedMonster].y) < 2000 and distance(heroData[i].x,heroData[i].y,monsterData[selectedMonster].x,monsterData[selectedMonster].y) < 1280):
        #
        #             print ("SPELL WIND",abs(base_x-17630),abs(base_y-9000))
        #         else:
        #             print("MOVE", abs(base_x-800), abs(base_y-800))
        #             continue
        #     if (i == 1):
        #         selectedMonster = 0
        #         for j in range(len(monsterData)):
        #             if (10*(1/(distance(heroData[i].x,heroData[i].y,monsterData[j].x,monsterData[j].y)+1)) + 10000*(1/(distance(base_x,base_y,monsterData[j].x,monsterData[j].y)+1)) + 5000*monsterData[j].near_base) > (10*(1/(distance(heroData[i].x,heroData[i].y,monsterData[selectedMonster].x,monsterData[selectedMonster].y)+1)) + 10000*(1/(distance(base_x,base_y,monsterData[selectedMonster].x,monsterData[selectedMonster].y)+1)) + 5000*monsterData[selectedMonster].near_base):
        #                 selectedMonster = j
        #
        #         #print(heroData[i])
        #         #print(monsterData[selectedMonster])
        #
        #         print("MOVE",monsterData[selectedMonster].x,monsterData[selectedMonster].y)
        #
        #     if (i == 2):
        #         if playerData[0][0] >= playerData[1][0]:
        #             if heroData[i].x != abs(base_x - 8815) and heroData[i].y != abs(base_y - 4500):
        #                 print ("MOVE " + str(int(abs(base_x - 8815))) + " " + str(int(abs(base_y - 4500))))
        #             else:
        #                 monsterID = 0
        #                 foundMonster = False
        #                 for j in range(len(monsterData)):
        #                     if distance(heroData[i].x,heroData[i].y,monsterData[j].x,monsterData[j].y) < 2200 and monsterData[j].threat_for != 2:
        #                         monsterID = j
        #                         foundMonster = True
        #                 if foundMonster:
        #                     #attackSector = randint(0, 2)
        #                     #if attackSector  == 0:
        #                     print ("SPELL CONTROL " + str(monsterData[monsterID].id) + " " +  str(abs(base_x - 17630)) +  " " + str(abs(base_y - 9000)))
        #                     #elif attackSector == 1:
        #                     #    print ("SPELL CONTROL " + str(monsterData[monsterID].id) + " " +  str(abs(base_x - 17630)) +  " " + str(abs(base_y - 9000)))
        #                     #elif attackSector == 2:
        #                     #    print ("SPELL CONTROL " + str(monsterData[monsterID].id) + " " +  str(abs(base_x - 17630)) +  " " + str(abs(base_y - 4500)))
        #                     #    continue
        #                 else:
        #                     monsterID = 0
        #                     for j in range(len(monsterData)):
        #                         if distance(heroData[i].x,heroData[i].y,monsterData[j].x,monsterData[j].y) < 2200 and monsterData[j].threat_for != 2:
        #                             monsterID = j
        #                     print("MOVE",monsterData[monsterID].x,monsterData[monsterID].y)
        #                     continue
        #         else:
        #             print("MOVE", abs(base_x-3500), abs(base_y-3500))
        #             continue
