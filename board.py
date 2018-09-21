import sys
import math

from entity import *
from board import *

def setUpBoard():
    base_x, base_y = [int(i) for i in input().split()]
    heroes_per_player = int(input())

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

    return BoardState(base_x,base_y,heroes_per_player,playerData[0],playerData[1],monsterData,heroData,enemyData,entity_count)

# Board State Class
class BoardState:
    def __init__(self,base_x,base_y,numHeroes,PlayerData,EnemyData,Monsters,Heros,Enemies,EntityCount):

        self.base_x = base_x
        self.base_y = base_y
        self.herosNum = numHeroes

        self.player      = [x for x in PlayerData]
        self.enemy       = [x for x in EnemyData]
        self.entities    = [{x.id : x for x in Monsters}, [x for x in Heros], {x.id : x for x in Enemies}]
        self.numEntity = EntityCount

    def setHeroStrategy(self,num,strategy):
        self.entities[1][num].strategy = strategy
    def value(self):
        return 0

    def nextState(self,Turn):
        returnType = BoardState(self.player,self.enemy,self.monsters,self.heros,self.enemies)
        returnType.takeTurn(turn)

        return returnType

    @staticmethod
    def copy(boardState):
        return BoardState(boardState.player,boardState.enemy,boardState.entities[0],boardState.entities[1],boardState.entities[2])

    def generateHeroMoves(self,heroNum):
        return self.entities[1][heroNum].generateActions(self)

    def takeTurn(self,Turn):
        if Turn.actionType == "WAIT":
            return

        if Turn.actionType == "SPELL":
            return

        if Turn.actionType == "MOVE":
            return

    def __str__(self):
        returnString = "Player:\n\tHealth: " + str(self.player[0]) + "\n\tMana: " + str(self.player[1]) + "\n\n"
        returnString += "Opponent:\n\tHealth: " + str(self.enemy[0]) + "\n\tMana: " + str(self.enemy[1]) + "\n\n"

        returnString += "Monsters: " + str(len(self.entities[0])) + "\n"
        for monsterID, monster in self.entities[0].items():
            returnString += "\t id: " + str(monsterID) + " -- " + str(monster) + "\n"
        returnString += "\n"

        returnString += "Heroes: " + str(len(self.entities[1])) + "\n"
        id = 0
        for hero in self.entities[1]:
            returnString += "\t id: " + str(id) + " -- " + str(hero) + "\n"
            id += 1
        returnString += "\n"

        returnString += "Enemies: " + str(len(self.entities[2])) + "\n"
        for enemyID, enemy in self.entities[2].items():
            returnString += "\t id: " + str(enemyID) + " -- " + str(enemy) + "\n"
        returnString += "\n"

        return returnString
