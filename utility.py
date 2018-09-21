import sys
import math

# Vector Class
class Vector:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.length = distance(self.x1,self.y1,self.x2,self.y2)

    def norm(self):
        self /= self.length

    def __mul__(self, amplitude):
        self.x2 *= amplitude
        self.y2 *= amplitude
        self.length *= amplitude

    def __div__(self, amplitude):
        self.x2 /= amplitude
        self.y2 /= amplitude
        self.length /= amplitude
