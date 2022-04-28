from abc import abstractmethod

from yaml import load

class Piece:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color
        self.image = None
    
    def move(self,x,y):
        if self.isLegalmove(x,y):
            self.x = x
            self.y = y
        else:
            print("Illegal Move")
    
    @abstractmethod
    def canMoveTo(self,x,y):
        pass

    @abstractmethod
    def loadImage(self,scale):
        pass