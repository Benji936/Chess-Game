import pygame
import copy

class Chessboard:
        
    def getPiece(self,x,y):
        index = x*8 + y
        return self.pieces.get(index,0)

    def changePositionOf(self,piece,x,y):
        self.pieces[x*8+y] = copy.copy(piece)
        del self.pieces[piece.x*8+piece.y]
        self.pieces[x*8+y].x = x
        self.pieces[x*8+y].y = y
        self.pieces[x*8+y].moved += 1

    def checkmate():
        pass

    def check():
        pass

    def __init__(self):
        self.pieces = {}
        self.moves = []

    #reverse display: you need just to substract by the size of height for y and width for x and get their absolute value to reverse the positions