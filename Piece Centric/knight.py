import pygame
from piece import Piece

directions = [(1,2),(2,1),(-1,2),(2,-1),(-2,1),(1,-2),(-1,-2),(-2,-1)]

class Knight(Piece):
    def isInMovingPattern(self,x,y):
        return abs(self.x-x) + abs(self.y-y) == 3 and (x != self.x and y != self.y)

    def somethingInTheWay(self,x,y,board):
        return 0

    def getPossibleMoves(self, board):
        self.moves = []
        for direction in directions:
            if self.canMoveTo(self.x+direction[0],self.y+direction[1],board):
                self.moves.append((self.x+direction[0],self.y+direction[1]))
            


    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_knight.png')
        img = pygame.transform.scale(img, (scale,scale))
        return img