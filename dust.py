import random
import numpy as np
class dust:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.connected = []
        self.newx = 0
        self.newy = 0
        self.direction()
    def direction(self):
        dir = random.randint(0,360)
        self.angle(dir)
    def angle(self,degree):
        if degree == 0:
            self.newx+=1
        if degree > 0 and degree < 90:
            self.newy+=1
            self.newx+=1
        if degree == 90:
            self.newx-=1
        if degree > 90 and degree < 180:
            self.newx-=1
            self.newy+=1
        if degree == 180:
            self.newx-=1
        if degree > 180 and degree < 270:
            self.newx-=1
            self.newy-=1
        if degree == 270:
            self.newy-=1
            self.newx-=1
        if degree == 360:
            self.newx+=1
    def move(self):
        self.x=self.x+self.newx
        self.y= self.y+self.newy
