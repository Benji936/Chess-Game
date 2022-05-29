import pygame
import copy
from bishop import Bishop
from knight import Knight
from moves import Promote, enPassant, Move
from piece import Piece
from queen import Queen
from rook import Rook

directions = [(1,1),(0,1),(-1,1),(0,2),(1,-1),(-1,-1),(0,-1),(0,-2)]

class Pawn(Piece):

    def canPassThrough(self,board,x,y):
        side = self.x-(self.x-x)
        beside = board.getPiece(side,self.y)
        if beside:
            if len(board.moves):
                lastTurnMovedPiece = board.getPiece(board.moves[-1].to[0],board.moves[-1].to[1])
            if beside.moved == 1 and 2 < beside.y < 5 and beside == lastTurnMovedPiece:
                return self.tryMove(board,enPassant(self,(x,y),(side,self.y)))
        return 0

    def canPromote(self,x,y):
        if y == 7 or y == 0:
            return [Promote(self,Queen(self.x,self.y,self.color),(x,y)),Promote(self,Bishop(self.x,self.y,self.color),(x,y)),Promote(self,Rook(self.x,self.y,self.color),(x,y)),Promote(self,Knight(self.x,self.y,self.color),(x,y))]
        return 0

    def canMoveTo(self,x,y,board):
        if self.isInMovingPattern(x,y):
            #Si le pion essaie d'aller en diagonale on vérifie s'il y'a une pièce a manger ou une prise en passant
            if self.x-x == 1 or self.x-x == -1:
                piece = board.getPiece(x,y)
                if piece:
                    if piece.color == self.color:
                        return 0
                    return self.tryMove(board,Move(self,(x,y)))
                else:
                    return self.canPassThrough(board,x,y)
            else:
                if self.somethingInTheWay(x,y,board):
                    return 0
                else:
                    piece = board.getPiece(x,y)
                    if not piece: 
                        return self.tryMove(board,Move(self,(x,y)))
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
        moves = []
        if(self.color == "black"):
            for i in range(0,4):
                dirX = self.x+directions[i][0]
                dirY = self.y+directions[i][1]
                move = self.canMoveTo(dirX,dirY,board)
                if move:
                    promotions = self.canPromote(dirX,dirY)
                    if promotions:
                        for promotion in promotions:
                            moves.append(promotion)
                    else:
                        moves.append(move)
        else:
            for i in range(4,8):
                dirX = self.x+directions[i][0]
                dirY = self.y+directions[i][1]
                move = self.canMoveTo(dirX,dirY,board)
                if move:
                    promotions = self.canPromote(dirX,dirY)
                    if promotions:
                        for promotion in promotions:
                            moves.append(promotion)
                    else:
                        moves.append(move)
        return moves
    
    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_pawn.png')
        img = pygame.transform.scale(img, (scale,scale))
        return img

    def __str__(self):
        return ""