import sys
import math

from entity import *
from board import *

# Functions
def distance(X1, Y1, X2, Y2):
    return ((X1 - X2) ** 2 + (Y1 - Y2) ** 2) ** .5


def truncateY(Object):
    if Object.y > 9000:
        Object.y = 9000

    if Object.y < 0:
        Object.y = 0

    Object.y = int(Object.y)


def truncateX(Object):
    if Object.x > 17630:
        Object.x = 17630

    if Object.x < 0:
        Object.x = 0

    Object.x = int(Object.x)

def setUpBoard():
    playerData  = []
    monsterData = []
    heroData    = []
    enemyData   = []

    for i in range(2):
        playerData.append([int(j) for j in input().split()])

    entity_count = int(input())

    for i in range(entity_count):
        current = [int(j) for j in input().split()]
        if current[1] == 0:
            monsterData.append(Monster(current[0],current[1],current[2],current[3],current[4],current[5],current[6],current[7],current[8],current[9],current[10]))
        if current[1] == 1:
            heroData.append(Hero(current[0],current[1],current[2],current[3],current[4],current[5]))
        if current[1] == 2:
            enemyData.append(Enemy(current[0],current[1],current[2],current[3],current[4],current[5]))

    return BoardState(playerData[0],playerData[1],monsterData,heroData,enemyData,entity_count)
