import pygame
from piece import Piece

class King(Piece):
    def canMoveTo(self,x,y):
        return (abs(self.y - y) == 1 or abs(self.x -x) == 1)


    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_king.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img