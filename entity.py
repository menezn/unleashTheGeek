import sys
import math

from roles import *

# Entity Classes
class Entity:
  def __init__(self, id, type, x, y, shield_life, is_controlled):
    idlist = ["monster", "ourhero", "opponenthero"]
    self.id = id
    self.type = type
    assert (type >= 0 and type <= 2), "invalid type for entity"
    self.entityasstring = idlist[type]
    self.x = x
    assert (x >= 0 and x <=17630 ), "invalid width (x)"
    self.y = y
    assert (y >= 0 and y <= 9000), "invalid height "
    self.shield_life = shield_life
    assert (shield_life >= 0 and shield_life <= 12), "invalid shield life"
    self.is_controlled = is_controlled
    assert (is_controlled == 0 or is_controlled == 1), "invalid shield life"

  def isValid(self):
    print ("In entity is valid")
    assert (type >= 0 and type <= 2), "invalid type for entity"
    assert (self.x >= 0 and self.x <=17630 ), "invalid width (x)"
    assert (self.y >= 0 and self.y <= 9000), "invalid height "
    assert (self.shield_life >= 0 and self.shield_life <= 12), "invalid shield life"
    assert (self.is_controlled == 0 or self.is_controlled == 1), "invalid shield life"

  def __str__(self):
    return "The entity attributes are %s" %(vars(self))

# id, type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for
class Monster(Entity):
    def __init__(self, id, type, x, y, shield_life, is_controlled,health, vx, vy, near_base, threat_for):
        Entity.__init__(self, id, type, x, y, shield_life, is_controlled)
        self.health = health
        self.near_base = near_base
        assert (near_base == 0 or near_base == 1), "invalid nearbase value"
        self.vx = vx
        assert (vx >= -17630 and vy <= 17630), "invalid velocity width (vx)"
        self.vy = vy
        assert (vx >= -9000 and vy <= 9000), "invalid velocity height (vy)"
        self.threat_for = threat_for
        if near_base == 0:
            assert(threat_for >= 0 and threat_for <= 2), "invalid threatfor for neabase = 0"
        else:
            assert(near_base == 1 or near_base == 2), "invalid threatfor for nearbase = 1"

    def willItNeverReachBase (self):
        return self.near_base == 0 and self.threat_for == 0

    def willItEventuallyReachBase (self):
        return self.near_base == 0 and self.threat_for == 1

    def willItEventuallyReachYourOpponentsBase (self):
        return self.near_base == 0 and self.threat_for == 2

    def isMonsterTargettingMyBase(self):
        return self.near_base == 1 and self.threat_for == 1

    def isMonsterTargettingOpponentBase(self):
        return self.threat_for == 1 and self.threat_for == 2

    def getDistanceFromOurBase(self, base_x, base_y):
        distance(self.x , self.y,base_x,base_y)

    def getDistanceFromOpponentBase(self, obase_x, obase_y):
        return distance(self.x,self.y,base_x,base_y)

    def getMonsterAtNextPosition(self):
        newMonster = copy.deepcopy(self)
        newMonster.x = newMonster.x + vx
        newMonster.y = newMonster.y + vy
        #setting the velocity of the new monster to 0
        newMonster.vx = 0
        newMonster.vy = 0
        return newMonster

    def isValid(self):
        super().isValid()
        assert (self.near_base == 0 or self.near_base == 1), "invalid nearbase value"
        assert (self.vx >= -17630 and self.vy <= 17630), "invalid velocity width (vx)"
        assert (self.vy >= -9000 and self.vy <= 9000), "invalid velocity height (vy)"
        if self.near_base == 0:
            assert (self.threat_for >= 0 and self.threat_for <= 2), "invalid threatfor for neabase = 0"
        else:
            assert (self.near_base == 1 or self.near_base == 2), "invalid threatfor for nearbase = 1"

    def __str__(self):
        return "The entity attributes are %s" %(vars(self))

class Hero(Entity):
    def __init__(self, id, type, x, y, shieldlife, isControl):
        Entity.__init__(self, id, type, x, y, shieldlife, isControl)
        self.strategy = None

    def manaGainedOutOfBox(self):
        return 0

    def generateActions(self,boardState):
        return self.strategy.returnTurns(boardState,self)

    def __str__(self):
        return "The entity attributes are %s" %(vars(self))

class Enemy(Entity):
    def __init__(self, id, type, x, y, shieldlife, isControl):
        Entity.__init__(self, id, type, x, y, shieldlife, isControl)

    def __str__(self):
        return "The entity attributes are %s" %(vars(self))
