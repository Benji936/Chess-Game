import pygame
import copy
from king import King
from queen import Queen
from bishop import Bishop
from rook import Rook
from knight import Knight
from pawn import Pawn


pieces = {"k" : King(0,0,"white"), "K" : King(0,0,"black"), "q" : Queen(0,0,"white"), "Q" : Queen(0,0,"black"), "b" : Bishop(0,0,"white"), 
"B":Bishop(0,0,"black"), "r" : Rook(0,0,"white"), "R" : Rook(0,0,"black"), "n" : Knight(0,0,"white"), "N" : Knight(0,0,"black"), 
"p" : Pawn(0,0,"white"), "P" : Pawn(0,0,"black")}

class Chessboard:

    def loadImages(self):
        for piece in self.pieces:
            piece.loadImage(self.scale)

    def convertStringInBoard(self,string):
        x = 0
        y = 0
        self.pieces = []
        for char in string:
            try:
                x += int(char)
            except:
                if char == "/":
                    y += 1
                    x = 0
                else:
                    pieces[char].x = x
                    pieces[char].y = y
                    self.pieces.append(copy.copy(pieces[char]))
                    x+=1
        



    def __init__(self,scale,start):
        self.images = {}
        self.pieces = []
        self.scale = scale 
        self.convertStringInBoard(start)
        self.loadImages()
    
    def display(self,screen):
        for piece in self.pieces:
            screen.blit(piece.image,(piece.x*self.scale,piece.y*self.scale))

