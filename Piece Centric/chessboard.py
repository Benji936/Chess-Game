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
keys = ["q","k","r","b","n","p"]
names = ["queen","king","rook","bishop","knight","pawn"]

class Chessboard:

    def loadImages(self,scale):
        for i in range(len(names)):
            white = pygame.image.load(r'sprites/white_' + names[i] +'.png')
            white = pygame.transform.scale(white, (scale,scale))
            self.images[keys[i]] = white

            black = pygame.image.load(r'sprites/black_' + names[i] +'.png')
            black = pygame.transform.scale(black, (scale,scale))
            self.images[keys[i].upper()] = black

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
        self.loadImages(scale)
        self.convertStringInBoard(start)
    
    def display(self,screen):
        for piece in self.pieces:
            for name in pieces:
                if type(pieces[name]) is type(piece) and pieces[name].color == piece.color:
                    screen.blit(self.images[name],(piece.x*self.scale,piece.y*self.scale))

