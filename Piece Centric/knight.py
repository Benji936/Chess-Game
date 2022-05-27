import pygame
from piece import Piece

directions = [(1,2),(2,1),(-1,2),(2,-1),(-2,1),(1,-2),(-1,-2),(-2,-1)]
columns = ["a","b","c","d","e","f","g","h"]

class Knight(Piece):
    def isInMovingPattern(self,x,y):
        return abs(self.x-x) + abs(self.y-y) == 3 and (x != self.x and y != self.y)

    def somethingInTheWay(self,x,y,board):
        return 0

    def getPossibleMoves(self, board):
        moves = []
        for direction in directions:
            move = self.canMoveTo(self.x+direction[0],self.y+direction[1],board)
            if move:
                moves.append(move)
        return moves
            


    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_knight.png')
        img = pygame.transform.scale(img, (scale,scale))
        return img

    def __str__(self):
        return "n" + str(columns[self.y]) + str(abs(self.x-8)) if self.color == "white" else "N"