import sys
import math

import functions

# Global Variables
sqrtTwo = 2**.5

# Action Classes
class Action:
    def __init__(self, sourceEntityID, sourceEntityType, actionType):
        self.sourceEntityID = sourceEntityID
        self.sourceEntityType = sourceEntityType
        self.actionType = actionType

    def __str__(self):
        assert(False)

    def takeTurn(self,BoardState):
        assert(False)

class Wait(Action):
    def __init__(self, sourceEntityID, sourceEntityType):
        Action.__init__(self,sourceEntityID,sourceEntityType,"WAIT")

    def __str__(self):
        return self.actionType

    def takeTurn(self,boardState):
        return BoardState.copy(boardState)

class Move(Action):
    def __init__(self, sourceEntityID,sourceEntityType, x1, y1):
        Action.__init__(self,sourceEntityID,sourceEntityType,"MOVE")
        self.x = x1
        self.y = y1

    def __str__(self):
        return self.actionType + " " + str(self.x) + " " + str(self.y)

    def takeTurn(self,boardState):
        nextIter = BoardState.copy(boardState)
        x1 = nextIter.entities[1][self.sourceEntityID].x
        y1 = nextIter.entities[1][self.sourceEntityID].y

        vec = Vector(x1,self.x,y1,self.y)
        if vec.length > 800:
            vec.norm()
            vec *=800

        nextIter.entities[1][self.sourceEntityID].x = truncateX(vec.x2)
        nextIter.entities[1][self.sourceEntityID].y = truncateY(vec.y2)

class Spell(Action):
    def __init__(self, sourceEntityID, sourceEntityType, spellType):
        Action.__init__(self,sourceEntityID,sourceEntityType,"SPELL")
        self.spellType = spellType

    def __str__(self):
        assert(False)

class Wind(Spell):
    def __init__(self, sourceEntityID,sourceEntityType, x1, y1):
        Spell.__init__(self,sourceEntityID,sourceEntityType,"WIND")
        self.x = x1
        self.y = y1

    def __str__(self):
        return self.actionType + " " + self.spellType +  " " + str(self.x) + " " + str(self.y)

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
    def __init__(self, sourceEntityID, targetEntityID,sourceEntityType, x1, y1):
        Spell.__init__(self,sourceEntityID,sourceEntityType,"CONTROL")
        self.targetEntityID = targetEntityID
        self.x = x1
        self.y = y1

    def toString():
        return self.actionType + " " + self.spellType + " " + str(targetEntityID) +  " " + str(self.x) + " " + str(self.y)

class Sheild(Spell):
    def __init__(self, sourceEntityID,sourceEntityType, targetEntityID, x1, y1):
        Spell.__init__(self,sourceEntityID,sourceEntityType,"SHEILD")
        self.targetEntityID = targetEntityID

    def __str__(self):
        return self.actionType + " " + self.spellType + " " + str(targetEntityID)
