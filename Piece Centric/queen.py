import pygame
from bishop import Bishop
from rook import Rook
from piece import Piece

class Queen(Piece):
    def canMoveTo(self,x,y):
        return (self.y == y or self.x ==x) or (abs(self.x-x) - abs(self.y-y) == 0)

    def somethingInTheWay(self,x,y,board):
        if(self.x == x and self.y == y): 
            return 1
        r = Rook(self.x,self.y,self.color)
        b = Bishop(self.x,self.y,self.color)
        if r.canMoveTo(x,y) and r.somethingInTheWay(x,y,board):
            return 1
        elif b.canMoveTo(x,y) and b.somethingInTheWay(x,y,board):
            return 1
        else: 
            return 0

    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_queen.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img