import pygame
from piece import Piece

class Knight(Piece):
    def canMoveTo(self,x,y):
        return abs(self.x-x) + abs(self.y-y) == 3

    def somethingInTheWay(self,x,y,board):
        return 0

    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_knight.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img