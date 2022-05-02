import pygame
from piece import Piece

class Rook(Piece):
    def canMoveTo(self,x,y):
        return (self.y == y or self.x ==x)


    def somethingInTheWay(self,x,y,board):

        if self.x > x:
            for i in range(x+1,self.x):
                if board.getPiece(i,y):
                    return 1
        elif self.x < x:
            for i in range(self.x+1,x):
                if board.getPiece(i,y):
                    return 1
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
        img = pygame.image.load(r'sprites/'+ self.color +'_rook.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img