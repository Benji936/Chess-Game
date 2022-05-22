import pygame
from bishop import Bishop
from rook import Rook
from piece import Piece

directions = [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(1,0),(-1,0),(0,-1)]

class Queen(Piece):
    def isInMovingPattern(self,x,y):
        return (self.y == y or self.x ==x) or (abs(self.x-x) - abs(self.y-y) == 0)

    def somethingInTheWay(self,x,y,board):
        if(self.x == x and self.y == y): 
            return 1
        r = Rook(self.x,self.y,self.color)
        b = Bishop(self.x,self.y,self.color)
        if r.isInMovingPattern(x,y) and r.somethingInTheWay(x,y,board):
            return 1
        elif b.isInMovingPattern(x,y) and b.somethingInTheWay(x,y,board):
            return 1
        else: 
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
        img = pygame.image.load(r'sprites/'+ self.color +'_queen.png')
        img = pygame.transform.scale(img, (scale,scale))
        return img