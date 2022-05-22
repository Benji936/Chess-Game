from abc import abstractmethod
import copy
from yaml import load

class Piece:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color
        self.moves = []
        self.moved = 0
    
    def canMoveTo(self,x,y,board):
        if self.isInMovingPattern(x,y):
            if self.somethingInTheWay(x,y,board) or board.outOfBounds(x,y):
                return 0

            piece = board.getPiece(x,y)
            if piece:
                if piece.color == self.color:
                    return 0
            return 1    
        else:
            return 0

    def move(self,x,y,board):
        if board.check() and (self != board.kings[0]):
            return 0

        canMove = self.canMoveTo(x,y,board)
        
        if canMove != 1 and canMove != 0:
            board.changePositionOf(self,x,y)
            board.changePositionOf(canMove[0],canMove[1][0],canMove[1][1])
            return 1
        elif canMove:
            board.changePositionOf(self,x,y)
            return 1
        return 0

    def display(self,screen,scale):
        screen.blit(self.loadImage(scale),(self.x*scale,self.y*scale))


    def canEat(self,x,y,board):
        return self.canMoveTo(x,y,board)

        
    def __eq__(self, other):
        return type(self) == type(other)
    
    @abstractmethod
    def somethingInTheWay(self,x,y,board):
        pass

    @abstractmethod
    def isInMovingPattern(self,x,y):
        pass

    @abstractmethod
    def getPossibleMoves(self,board):
        pass

    @abstractmethod
    def loadImage(self,scale):
        pass