import pygame
import copy
from piece import Piece

class Pawn(Piece):

    #Override move for pawn because he is specific

    def move(self,x,y,board):
        if self.canMoveTo(x,y):
            
            if self.x-x == 1 or self.x-x == -1:
                piece = board.getPiece(x,y)
                if piece:
                    if piece.color == self.color:
                        return 0
                    board.pieces[x*8+y] = copy.copy(self)
                    del board.pieces[self.x*8+self.y]
                    board.pieces[x*8+y].x = x
                    board.pieces[x*8+y].y = y
                    return 1
                else:
                    return 0
            else:
                if self.somethingInTheWay(x,y,board):
                    return 0
                else:
                    piece = board.getPiece(x,y)
                    if not piece:
                        board.pieces[x*8+y] = copy.copy(self)
                        del board.pieces[self.x*8+self.y]
                        board.pieces[x*8+y].x = x
                        board.pieces[x*8+y].y = y
                        return 1
                    return 0
        return 0

    def canMoveTo(self,x,y):
        if self.color == "black":
            if self.y != 1:
                return y-self.y == 1 and (-2 < self.x-x < 2)
            else:
                return (0 < y-self.y < 3)
        else:
            if self.y != 6:
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