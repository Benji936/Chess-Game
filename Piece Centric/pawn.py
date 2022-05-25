import pygame
import copy
from piece import Piece

directions = [(1,1),(0,1),(-1,1),(0,2),(1,-1),(-1,-1),(0,-1),(0,-2)]

class Pawn(Piece):

    def canPassThrough(self,board,x,y):
        side = self.x-(self.x-x)
        beside = board.getPiece(side,self.y)
        if beside:
            if beside.moved == 1 and 2 < beside.y < 5:
                #board.changePositionOf(self,x,y)
                #del board.pieces[side*8+self.y]
                return (side,self.y)
        return 0

    def promote(self):
        pass

    def canMoveTo(self,x,y,board):
        if self.isInMovingPattern(x,y):
            if self.x-x == 1 or self.x-x == -1:
                piece = board.getPiece(x,y)
                if piece:
                    if piece.color == self.color:
                        return 0
                    #board.changePositionOf(self,x,y)
                    checkBoard = copy.deepcopy(board)
                    checkBoard.changePositionOf(self,x,y)
                    if checkBoard.check():
                        return 0
                    return 1
                else:
                    return self.canPassThrough(board,x,y)
            else:
                if self.somethingInTheWay(x,y,board):
                    return 0
                else:
                    piece = board.getPiece(x,y)
                    if not piece:
                        #board.changePositionOf(self,x,y)  
                        checkBoard = copy.deepcopy(board)
                        checkBoard.changePositionOf(self,x,y)
                        if checkBoard.check():
                            return 0
                        return 1
                    return 0
        return 0
    
    

    def isInMovingPattern(self,x,y):
        if self.color == "black":
            if self.moved:
                return y-self.y == 1 and (-2 < self.x-x < 2)
            else:
                return 0 < y-self.y < 3 and (-2 < self.x-x < 2)
        else:
            if self.moved:
                return self.y-y == 1 and (-2 < self.x-x < 2)
            else:
                return 0 < self.y-y < 3 and (-2 < self.x-x < 2)


    def somethingInTheWay(self,x,y,board):
        if self.y > y:
            for i in range(y+1,self.y):
                if board.getPiece(x,i):
                    return 1
        elif self.y < y:
            for i in range(self.y+1,y):
                if board.getPiece(x,i):
                    return 1
        return 0


    def getPossibleMoves(self, board):
        self.moves = []
        if(self.color == "black"):
            for i in range(0,4):
                if self.canMoveTo(self.x+directions[i][0],self.y+directions[i][1],board):
                    self.moves.append((self.x+directions[i][0],self.y+directions[i][1]))
        else:
            for i in range(4,8):
                if self.canMoveTo(self.x+directions[i][0],self.y+directions[i][1],board):
                    self.moves.append((self.x+directions[i][0],self.y+directions[i][1]))
        return self.moves
    
    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_pawn.png')
        img = pygame.transform.scale(img, (scale,scale))
        return img

    def __str__(self):
        return ""