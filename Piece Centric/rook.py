import pygame
from piece import Piece

class Rook(Piece):
    def canMoveTo(self,x,y):
        return (self.y == y or self.x ==x)

    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_rook.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img