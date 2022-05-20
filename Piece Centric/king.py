import pygame
import copy
from chessboard import Chessboard
from rook import Rook
from piece import Piece

directions = [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(1,0),(-1,0),(0,-1)]

class King(Piece):
    def isInMovingPattern(self,x,y):
        return (abs(self.y - y) < 2 and abs(self.x -x) < 2)

    
    def canMoveTo(self,x,y,board):
        #Check if the king moves normaly 
        if(not super().canMoveTo(x,y,board)):
            difX = x-self.x
            difY = y-self.y
            #Then if the king wants to ROC
            if(abs(difX) == 2 and difY == 0 and not self.moved):
                difX = int(difX/abs(difX))
                r = Rook(self.x,self.y,"white")
                rockPos = int((difX+1)*3.5)
                if not r.somethingInTheWay(rockPos,self.y,board) and not self.somethingInTheWay(rockPos,self.y,board):

                    r = board.getPiece(rockPos,self.y)
                    return [r,(x + difX*(-1),y)]
            return 0
        return 1
        

    def somethingInTheWay(self,x,y,board):

        tempBoard = Chessboard()
        board.copyTo(tempBoard)
        del tempBoard.pieces[self.x*8+self.y]
        king = copy.copy(self)
        king.x = x
        king.y = y
        tempBoard.pieces[x*8+y] = king
        
        for direction in directions:
            count = 1
            #Tant qu'on reste dans le plateau pendant le parcours
            while x+count*direction[0] < 8 and y+count*direction[1] < 8 and x+count*direction[0] >= 0 and y+count*direction[1] >=0:
                piece = tempBoard.getPiece(x+count*direction[0],y+count*direction[1])
                if piece and piece.color != self.color:
                    if piece.canMoveTo(x,y,tempBoard) and not piece.somethingInTheWay(x,y,tempBoard):
                        return 1
                count += 1

        return 0

    def getPossibleMoves(self, board):
        self.moves = []
        for direction in directions:
            count = 1
            xDirection = self.x+count*direction[0]
            yDirection = self.y+count*direction[1]
            #Tant qu'on reste dans le plateau pendant le parcours
            while xDirection < 8 and yDirection < 8 and xDirection >= 0 and yDirection >= 0:
                if self.canMoveTo(xDirection,yDirection,board):
                    self.moves.append((xDirection,yDirection))
                count += 1
                xDirection = self.x+count*direction[0]
                yDirection = self.y+count*direction[1]


    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_king.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img