from abc import abstractmethod

from yaml import load

class Piece:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color
        self.image = None
    
    def move(self,x,y):
        if self.canMoveTo(x,y):
            self.x = x
            self.y = y
            return 1
        else:
            return 0

    def display(self,screen,scale):
        screen.blit(self.image,(self.x*scale,self.y*scale))
        
    
    @abstractmethod
    def canMoveTo(self,x,y):
        pass

    @abstractmethod
    def loadImage(self,scale):
        pass