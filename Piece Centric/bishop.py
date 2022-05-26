import pygame
from piece import Piece

directions = [(1,1),(-1,-1),(-1,1),(1,-1)]

class Bishop(Piece):
    def isInMovingPattern(self,x,y):
        return not (abs(self.x-x) - abs(self.y-y))

    def somethingInTheWay(self,x,y,board):
        if(self.x == x and self.y == y): 
            return 1
        x_mov = (x-self.x) / abs(x-self.x) 
        y_mov = (y-self.y) / abs(y-self.y) 
        i = 1
        while(self.x + i*x_mov != x and self.y + i*y_mov != y):
            piece = board.getPiece(self.x + i*x_mov,self.y + i*y_mov)
            if piece:
                return 1
            i+=1

    def getPossibleMoves(self, board):
        moves = []
        for direction in directions:
            count = 1
            xDirection = self.x+count*direction[0]
            yDirection = self.y+count*direction[1]
            #Tant qu'on reste dans le plateau pendant le parcours
            while xDirection < 8 and yDirection < 8 and xDirection >= 0 and yDirection >= 0:
                move = self.canMoveTo(xDirection,yDirection,board)
                if move:
                    moves.append(move)
                count += 1
                xDirection = self.x+count*direction[0]
                yDirection = self.y+count*direction[1]
        return moves
        

    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_bishop.png')
        img = pygame.transform.scale(img, (scale,scale))
        return img
    

            