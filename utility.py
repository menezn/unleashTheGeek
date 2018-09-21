import sys
import math
import copy

from functions import *
# Vector Class
class Vector:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.translateToOrigin()
        self.length = distance(self.x1,self.y1,self.x2,self.y2)

    def norm(self):
        return self / self.length

    def __mul__(self, amplitude):
        returnType = copy.deepcopy(self)

        returnType.x2 *= amplitude
        returnType.y2 *= amplitude
        returnType.length *= amplitude

        return returnType

    def __truediv__(self, amplitude):
        returnType = copy.deepcopy(self)

        returnType.x1 /= amplitude
        returnType.y1 /= amplitude
        returnType.x2 /= amplitude
        returnType.y2 /= amplitude
        returnType.length /= amplitude

        return returnType

    def truncate(self):
        self.x1 = int(self.x1)
        self.x2 = int(self.x2)
        self.y1 = int(self.y1)
        self.y2 = int(self.y2)

    def translateToOrigin(self):
        self.x2 = self.x2 - self.x1
        self.x1 = self.x1 - self.x1
        self.y2 = self.y2 - self.y1
        self.y1 = self.y1 - self.y1

    def __str__(self):
        return "(" + str(self.x1) + ", " + str(self.y1) +  ") (" + str(self.x2) + ", " + str(self.y2) + ")"
