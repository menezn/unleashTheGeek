import sys
import math

from action import *

class Tank:
    def __init__(self):
        self.turns = []

    def wind(self,boardState,entity):
        turnList = []

        turnList.append(Wind(entity.id, entity.type, 2000, 0))
        turnList.append(Wind(entity.id, entity.type, 1000*sqrtTwo, -1000*sqrtTwo))

        turnList.append(Wind(entity.id, entity.type, 0, -2000))
        turnList.append(Wind(entity.id, entity.type, -1000*sqrtTwo, -1000*sqrtTwo))

        turnList.append(Wind(entity.id, entity.type, -2000, 0))
        turnList.append(Wind(entity.id, entity.type, -1000*sqrtTwo, 1000*sqrtTwo))

        turnList.append(Wind(entity.id, entity.type, 0, 2000))
        turnList.append(Wind(entity.id, entity.type, 1000*sqrtTwo, 1000*sqrtTwo))

        return turnList

    def followEnemy(self,boardState,entity):
        turnList = []

        for enemy in boardState.entities[0]:
            turnList.append(Move(entity.id, entity.type, enemy.x, enemy.y))

        for enemy in boardState.entities[2]:
            turnList.append(Move(entity.id, entity.type, enemy.x, enemy.y))

        return turnList


    def goToLocation(self,boardState,entity):
        turnList = []

        turnList.append(Move(entity.id, entity.type, 2000, 0))
        turnList.append(Move(entity.id, entity.type, 1000*sqrtTwo, -1000*sqrtTwo))

        turnList.append(Move(entity.id, entity.type, 0, -2000))
        turnList.append(Move(entity.id, entity.type, -1000*sqrtTwo, -1000*sqrtTwo))

        turnList.append(Move(entity.id, entity.type, -2000, 0))
        turnList.append(Move(entity.id, entity.type, -1000*sqrtTwo, 1000*sqrtTwo))

        turnList.append(Move(entity.id, entity.type, 0, 2000))
        turnList.append(Move(entity.id, entity.type, 1000*sqrtTwo, 1000*sqrtTwo))

        return turnList

    def wait(self,entity):
        turnList = []

        turnList.append(Wait(entity.id, entity.type))

        return turnList

    def returnTurns(self,boardState,entity):
        turnList = []

        turnList += self.wind(boardState,entity)
        turnList += self.followEnemy(boardState,entity)
        turnList += self.goToLocation(boardState,entity)
        turnList += self.wait(entity)

        return turnList
