import sys
import math

from action import *
from functions import *

class Tank:
    def __init__(self):
        self.turns = []

    def wind(self,boardState,entity):
        turnList = []
        if boardState.player[1] > 10:
            turnList.append(Wind(entity, entity.x+2000,         entity.y+0))
            turnList.append(Wind(entity, entity.x+1000*sqrtTwo, entity.y+1000*sqrtTwo))

            turnList.append(Wind(entity, entity.x+0,            entity.y+2000))
            turnList.append(Wind(entity, entity.x-1000*sqrtTwo, entity.y+1000*sqrtTwo))

            turnList.append(Wind(entity, entity.x-2000,         entity.y+0))
            turnList.append(Wind(entity, entity.x-1000*sqrtTwo, entity.y+1000*sqrtTwo))

            turnList.append(Wind(entity, entity.x+0,            entity.y+2000))
            turnList.append(Wind(entity, entity.x+1000*sqrtTwo, entity.y+1000*sqrtTwo))

        return turnList

    def followEnemy(self,boardState,entity):
        turnList = []

        for enemyID,enemy in boardState.entities[0].items():
            turnList.append(Move(entity, enemy.x, enemy.y))

        for enemyID,enemy  in boardState.entities[2].items():
            turnList.append(Move(entity, enemy.x, enemy.y))

        return turnList


    def goToLocation(self,boardState,entity):
        turnList = []

        turnList.append(Move(entity, entity.x+2000,         entity.y+0))
        turnList.append(Move(entity, entity.x+1000*sqrtTwo, entity.y-1000*sqrtTwo))

        turnList.append(Move(entity, entity.x+0,            entity.y-2000))
        turnList.append(Move(entity, entity.x-1000*sqrtTwo, entity.y-1000*sqrtTwo))

        turnList.append(Move(entity, entity.x-2000,         entity.y+0))
        turnList.append(Move(entity, entity.x-1000*sqrtTwo, entity.y+1000*sqrtTwo))

        turnList.append(Move(entity, entity.x+0,            entity.y+2000))
        turnList.append(Move(entity, entity.x+1000*sqrtTwo, entity.y+1000*sqrtTwo))

        return turnList

    def wait(self,entity):
        turnList = []

        turnList.append(Wait(entity))

        return turnList

    def returnTurns(self,boardState,entity):
        turnList = []

        turnList += self.wind(boardState,entity)
        turnList += self.followEnemy(boardState,entity)
        turnList += self.goToLocation(boardState,entity)
        turnList += self.wait(entity)

        return turnList

class SpellCaster:
    def __init__(self):
        self.turns = []

    def wind(self,boardState,entity):
        turnList = []
        if boardState.player[1] > 10:
            turnList.append(Wind(entity, entity.x+2000,         entity.y+0))
            turnList.append(Wind(entity, entity.x+1000*sqrtTwo, entity.y+1000*sqrtTwo))

            turnList.append(Wind(entity, entity.x+0,            entity.y+2000))
            turnList.append(Wind(entity, entity.x-1000*sqrtTwo, entity.y+1000*sqrtTwo))

            turnList.append(Wind(entity, entity.x-2000,         entity.y+0))
            turnList.append(Wind(entity, entity.x-1000*sqrtTwo, entity.y+1000*sqrtTwo))

            turnList.append(Wind(entity, entity.x+0,            entity.y+2000))
            turnList.append(Wind(entity, entity.x+1000*sqrtTwo, entity.y+1000*sqrtTwo))

        return turnList

    def control(self,boardState,entity):
        turnList = []

        if boardState.player[1] > 10:
            ViableTargets = [enemy for id,enemy in boardState.entities[0].items() if distance(entity.x,entity.y,enemy.x,enemy.y) < 2200 and enemy.is_controlled != 1] + [enemy for id,enemy in boardState.entities[2].items() if distance(entity.x,entity.y,enemy.x,enemy.y) < 2200 and enemy.is_controlled != 1]
            for target in ViableTargets:
                turnList.append(Control(entity, target, target.x+2000,         target.y+0))
                turnList.append(Control(entity, target, target.x+1000*sqrtTwo, target.y+1000*sqrtTwo))

                turnList.append(Control(entity, target, target.x+0,            target.y+2000))
                turnList.append(Control(entity, target, target.x-1000*sqrtTwo, target.y+1000*sqrtTwo))

                turnList.append(Control(entity, target, target.x-2000,         target.y+0))
                turnList.append(Control(entity, target, target.x-1000*sqrtTwo, target.y+1000*sqrtTwo))

                turnList.append(Control(entity, target, target.x+0,            target.y+2000))
                turnList.append(Control(entity, target, target.x+1000*sqrtTwo, target.y+1000*sqrtTwo))

                turnList.append(Control(entity, target, target.x+abs(boardState.base_x-17630), target.y+abs(boardState.base_y-9000)))

        return turnList

    def shield(self,boardState,entity):
        turnList = []

        if boardState.player[1] > 10:
            ViableTargets = [enemy for id,enemy in boardState.entities[0].items() if distance(entity.x,entity.y,enemy.x,enemy.y) < 2200 and enemy.shield_life == 0] + [hero for hero in boardState.entities[1] if distance(entity.x,entity.y,hero.x,hero.y) < 2200 and hero.shield_life == 0] + [enemy for id,enemy in boardState.entities[2].items() if distance(entity.x,entity.y,enemy.x,enemy.y) < 2200 and enemy.shield_life == 0]
            for target in ViableTargets:
                turnList.append(Shield(entity, target.id))


        return turnList

    def followEnemy(self,boardState,entity):
        turnList = []

        for id,enemy in boardState.entities[0].items():
            turnList.append(Move(entity, enemy.x, enemy.y))

        for id,enemy in boardState.entities[2].items():
            turnList.append(Move(entity, enemy.x, enemy.y))

        return turnList


    def goToLocation(self,boardState,entity):
        turnList = []

        turnList.append(Move(entity, entity.x+2000,         entity.y+0))
        turnList.append(Move(entity, entity.x+1000*sqrtTwo, entity.y-1000*sqrtTwo))

        turnList.append(Move(entity, entity.x+0,            entity.y-2000))
        turnList.append(Move(entity, entity.x-1000*sqrtTwo, entity.y-1000*sqrtTwo))

        turnList.append(Move(entity, entity.x-2000,         entity.y+0))
        turnList.append(Move(entity, entity.x-1000*sqrtTwo, entity.y+1000*sqrtTwo))

        turnList.append(Move(entity, entity.x+0,            entity.y+2000))
        turnList.append(Move(entity, entity.x+1000*sqrtTwo, entity.y+1000*sqrtTwo))

        return turnList

    def wait(self,entity):
        turnList = []

        turnList.append(Wait(entity))

        return turnList

    def returnTurns(self,boardState,entity):
        turnList = []

        turnList += self.wind(boardState,entity)
        turnList += self.control(boardState,entity)
        turnList += self.shield(boardState,entity)
        turnList += self.followEnemy(boardState,entity)
        turnList += self.goToLocation(boardState,entity)
        turnList += self.wait(entity)

        return turnList
