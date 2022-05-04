import pygame
import copy
from piece import Piece

class Pawn(Piece):

    def passThrough(self,board,x,y):
        side = self.x-(self.x-x)
        beside = board.getPiece(side,self.y)
        if beside:
            if beside.moved == 1 and 2 < beside.y < 5:
                board.changePositionOf(self,x,y)
                del board.pieces[side*8+self.y]
                return 1
        return 0

    def move(self,x,y,board):
        if self.canMoveTo(x,y):
            if self.x-x == 1 or self.x-x == -1:
                piece = board.getPiece(x,y)
                if piece:
                    if piece.color == self.color:
                        return 0
                    board.changePositionOf(self,x,y)
                    return 1
                else:
                    return self.passThrough(board,x,y)
            else:
                if self.somethingInTheWay(x,y,board):
                    return 0
                else:
                    piece = board.getPiece(x,y)
                    if not piece:
                        board.changePositionOf(self,x,y)  
                        return 1
                    return 0
        return 0

    def canMoveTo(self,x,y):
        if self.color == "black":
            if self.moved:
                return y-self.y == 1 and (-2 < self.x-x < 2)
            else:
                return (0 < y-self.y < 3)
        else:
            if self.moved:
                return self.y-y == 1 and (-2 < self.x-x < 2)
            else:
                return 0 < self.y-y < 3 


    def somethingInTheWay(self,x,y,board):
        if self.y > y:
            for i in range(y+1,self.y):
                if board.getPiece(x,i):
                    return 1
        elif self.y < y:
            for i in range(self.y+1,y):
                if board.getPiece(x,i):
                    return 1
        return 0
    
    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_pawn.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img