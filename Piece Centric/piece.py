from abc import abstractmethod
import copy

from moves import Move

class Piece:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color
        self.moved = 0

    def tryMove(self,board,move):
        boardCopy = copy.deepcopy(board)
        boardCopy.changePositionOf(self,move.to[0],move.to[1])
        if boardCopy.check():
            return 0
        return move
    
    def canMoveTo(self,x,y,board):
        if self.isInMovingPattern(x,y):
            if self.somethingInTheWay(x,y,board) or board.outOfBounds(x,y):
                return 0

            piece = board.getPiece(x,y)
            if piece:
                if piece.color == self.color:
                    return 0

            return self.tryMove(board,Move(self,(x,y)))
        else:
            return 0


    def move(self,x,y,board,promotion=0):
        move = self.canMoveTo(x,y,board)
        if move:
            if promotion:
                promotion.applyMove(board)
            else:
                move.applyMove(board)
            return 1
        return 0


    def display(self,screen,scale):
        screen.blit(self.loadImage(scale),(self.x*scale,self.y*scale))


    def canEat(self,x,y,board):
        return self.canMoveTo(x,y,board)

        
    def __eq__(self, other):
        return type(self) == type(other) and self.x == other.x and self.y == other.y

    def __str__(self):
        colors = {"white":0,"black":1}
        
        return repr(self).split('<')[1].split('.')[colors[self.color]][0]

    
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