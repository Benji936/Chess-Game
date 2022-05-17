import pygame
import copy
from rook import Rook
from piece import Piece

class King(Piece):
    def canMoveTo(self,x,y):
        return (abs(self.y - y) == 1 or abs(self.x -x) == 1)

    
    def move(self,x,y,board):
        #Check if the king moves normaly 
        if(not super().move(x,y,board)):
            difX = x-self.x
            difY = y-self.y
            #Then if the king wants to ROC
            if(abs(difX) == 2 and not difY):

                difX = int(difX/abs(difX))
                r = Rook(self.x,self.y,"white")
                rockPos = int((difX+1)*3.5)

                if not r.somethingInTheWay(rockPos,self.y,board):
                    board.changePositionOf(self,x,y)
                    r = board.getPiece(rockPos,self.y)
                    newPos = board.getPiece(x,y)
                    board.changePositionOf(r,newPos.x + difX*(-1),newPos.y)
                    return 1
            return 0
        return 1
        

    def somethingInTheWay(self,x,y,board):
        directions = [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(1,0),(-1,0),(0,-1)]
        for direction in directions:
            count = 1
            #Tant qu'on reste dans le plateau pendant le parcours
            while x+count*direction[0] < 8 and y+count*direction[1] < 8 and x+count*direction[0] > 0 and y+count*direction[1] > 0:
                piece = board.getPiece(x+count*direction[0],y+count*direction[1])
                if piece and piece.color != self.color:
                    if piece.canMoveTo(x,y) and not piece.somethingInTheWay(x,y,board):
                        return 1
                count += 1

        return 0


    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_king.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img