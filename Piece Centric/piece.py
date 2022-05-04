from abc import abstractmethod
import copy
from yaml import load

class Piece:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color
        self.moved = 0
        self.image = None
    
    def move(self,x,y,board):
        if self.canMoveTo(x,y):
            if self.somethingInTheWay(x,y,board):
                return 0

            piece = board.getPiece(x,y)
            if piece:
                if piece.color == self.color:
                    return 0
            board.changePositionOf(self,x,y)   
            return 1
        else:
            return 0

    def display(self,screen,scale):
        screen.blit(self.image,(self.x*scale,self.y*scale))
        
    
    @abstractmethod
    def somethingInTheWay(self,x,y,board):
        pass

    @abstractmethod
    def canMoveTo(self,x,y):
        pass

    @abstractmethod
    def loadImage(self,scale):
        pass