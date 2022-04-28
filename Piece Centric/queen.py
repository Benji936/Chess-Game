import pygame
from piece import Piece

class Queen(Piece):
    def canMoveTo(self,x,y):
        return (self.y == y or self.x ==x) or (abs(self.x-x) - abs(self.y-y) == 0)

    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_queen.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img