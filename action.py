import sys
import math

from functions import *
from utility import *

# Global Variables
sqrtTwo = 2**.5

# Action Classes
class Action:
    def __init__(self, entity, actionType):
        self.sourceEntityID = entity.id
        self.sourceEntityType = entity.type
        self.actionType = actionType

    def __str__(self):
        assert(False)

    def takeTurn(self,BoardState):
        assert(False)

class Wait(Action):
    def __init__(self, entity):
        Action.__init__(self,entity,"WAIT")

    def __str__(self):
        return self.actionType

    def takeTurn(self,boardState):
        return BoardState.copy(boardState)

class Move(Action):
    def __init__(self, entity, x1, y1):
        Action.__init__(self,entity,"MOVE")
        self.x1 = entity.x
        self.y1 = entity.y
        self.x2 = x1
        self.y2 = y1

        self.vec = Vector(self.x1,self.y1,self.x2,self.y2)

        if entity.type == 0 and self.vec.length > 400:
            self.vec = self.vec.norm()
            self.vec *= 400
        elif self.vec.length > 800:
            self.vec = self.vec.norm()
            self.vec *= 800

        self.vec.truncate()

    def __str__(self):
        return self.actionType + " " + str(self.x1+self.vec.x2) + " " + str(self.y1+self.vec.y2)

    def takeTurn(self,boardState):
        nextIter = BoardState.copy(boardState)
        x1 = nextIter.entities[1][self.sourceEntityID].x
        y1 = nextIter.entities[1][self.sourceEntityID].y

        nextIter.entities[1][self.sourceEntityID].x = truncateX(vec.x2)
        nextIter.entities[1][self.sourceEntityID].y = truncateY(vec.y2)

class Spell(Action):
    def __init__(self, entity, spellType):
        Action.__init__(self,entity,"SPELL")
        self.spellType = spellType

    def __str__(self):
        assert(False)

class Wind(Spell):
    def __init__(self, entity, x1, y1):
        Spell.__init__(self,entity,"WIND")
        self.x1 = entity.x
        self.y1 = entity.y
        self.x2 = x1
        self.y2 = y1

        self.vec = Vector(self.x1,self.y1,self.x2,self.y2)

        if self.vec.length != 2200:
            self.vec = self.vec.norm()
            self.vec *= 2200

        self.vec.truncate()

    def __str__(self):
        return self.actionType + " " + self.spellType +  " " + str(self.x1+self.vec.x2) + " " + str(self.y1+self.vec.y2)

    def takeTurn(self, current_board_state):
        future_board_state = copy.deepcopy(current_board_state)
        # windspell is cast by the source entity
        board_state = BoardState()
        board_state.getHerosIdDic()
        windspellCasterDict = future_board_state.getHerosIdDic()
        windSpellCaster = windspellCasterDict[self.sourceEntityID]
        monsterDict = board_state.getMonsterIdDic()
        abc = Monster()
        abc.moveMonsterToNewPosition()
        for monsterId, monsterObj in monsterDict:
            if distance(windSpellCaster.x,windSpellCaster.y,monsterObj.x,monsterObj.y) <= 1280:
                vec = Vector(windSpellCaster.x, windSpellCaster.y, x1, y1)
                vec.x1 = 0
                vec.y1 = 0
                vec.x2 = (x1-windSpellCaster.x)/vec.length
                vec.y1 = (y1-windSpellCaster.y)/vec.length
                vec.x2 *= 2200
                vec.y2 *= 2200
                monsterObj.moveMonsterToNewPosition(vec.x2, vec.y1)
                monsterObj.is_velocity_invalid = True

        #for monsterData

class Control(Spell):
    def __init__(self, entity, targetEntity, x1, y1):
        Spell.__init__(self,entity,"CONTROL")
        self.targetEntityID = targetEntity.id
        self.x1 = targetEntity.x
        self.y1 = targetEntity.y
        self.x2 = x1
        self.y2 = y1

        self.vec = Vector(self.x1,self.y1,self.x2,self.y2)

        if entity.type == 0 and self.vec.length > 400:
            self.vec = self.vec.norm()
            self.vec *= 400
        elif self.vec.length > 800:
            self.vec = self.vec.norm()
            self.vec *= 800

        self.vec.truncate()

    def __str__(self):
        return self.actionType + " " + self.spellType + " " + str(self.targetEntityID) +  " " + str(self.x1+self.vec.x2) + " " + str(self.y1+self.vec.y2)

class Shield(Spell):
    def __init__(self, entity, targetEntityID):
        Spell.__init__(self,entity,"SHEILD")
        self.targetEntityID = targetEntityID

    def __str__(self):
        return self.actionType + " " + self.spellType + " " + str(self.targetEntityID)
