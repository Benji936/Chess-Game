import pygame
from king import King
import copy

class Chessboard:
        
    def getPiece(self,x,y):
        index = x*8 + y
        return self.pieces.get(index,0)

    def changePositionOf(self,piece,x,y):
        if self.check() and type(piece) != type(King(0,0,"white")):
            return 0

        self.pieces[x*8+y] = copy.copy(piece)
        del self.pieces[piece.x*8+piece.y]
        self.pieces[x*8+y].x = x
        self.pieces[x*8+y].y = y
        self.pieces[x*8+y].moved += 1
        return 1

    def checkmate(self):
        pass

    def check(self):
        king = self.kings[(self.turn+1)%2]
        return king.somethingInTheWay(king.x,king.y,self)

    def nexTurn(self,piece,x,y):
        if(piece.move(x,y,self)):
            self.turn += 1
            return 1
        return 0

    def wichColorTurn(self):
        return self.colors[self.turn%2]

    def __init__(self):
        self.colors = ["white","black"]
        self.turn = 0
        self.kings = []
        self.pieces = {}
        self.moves = []

    #reverse display: you need just to substract by the size of height for y and width for x and get their absolute value to reverse the positions