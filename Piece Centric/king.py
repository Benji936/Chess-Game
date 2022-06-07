import pygame
import copy
from chessboard import Chessboard
from rook import Rook
from pawn import Pawn
from piece import Piece
from moves import Castle, Move

directions = [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(1,0),(-1,0),(0,-1)]

class King(Piece):
    def isInMovingPattern(self,x,y):
        return (abs(self.y - y) < 2 and abs(self.x -x) < 2)

    
    def canMoveTo(self,x,y,board):
        move = super().canMoveTo(x,y,board)
        #Check if the king can move normaly 
        if(not move):
            difX = x-self.x
            difY = y-self.y
            #Then if the king wants to ROC
            if(abs(difX) == 2 and difY == 0 and not self.moved):
                #Scale the dif to -1 or 1 wether it's left or right
                difX = int(difX/abs(difX))
                r = Rook(self.x,self.y,"white")
                #if difX = -1 -> (-1 + 1)*3.5 = 0 so we get the position x of the left rook | if difX = 1 -> (1+1)*3.5 = 7 we get the position x of the right rook
                rookPos = int((difX+1)*3.5)
                if not r.somethingInTheWay(rookPos,self.y,board) and self.tryMove(board,Move(self,(self.x+difX,self.y))) and self.tryMove(board,Move(self,(self.x+(difX*2),self.y))):

                    r = board.getPiece(rookPos,self.y)
                    if not r:
                        return 0
                    if r.moved:
                        return 0
                    return Castle(self,(x,y),r,(x + difX*(-1),y))
            return 0
        return move
        

    def somethingInTheWay(self,x,y,board):
        for piece in board.pieces.values():
            if piece.color != self.color:
                if piece.canMoveTo(x,y,board) and not piece.somethingInTheWay(x,y,board):
                    return 1
        return 0

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
        img = pygame.image.load(r'sprites/'+ self.color +'_king.png')
        img = pygame.transform.scale(img, (scale,scale))
        return img