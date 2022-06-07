from king import King
from queen import Queen
from bishop import Bishop
from rook import Rook
from knight import Knight
from pawn import Pawn


import copy
import pygame
from pygame.locals import *


white = (255,249,201)
selected_white = (255,215,162)
black = (114,162,86)
selected_black = (165,223,121)
initScale = 800
size = initScale, initScale
cellScale = int(initScale/8)
colors = ["white","black"]

pieces = {"k" : King(0,0,colors[0]), "K" : King(0,0,colors[1]), "q" : Queen(0,0,colors[0]), "Q" : Queen(0,0,colors[1]), "b" : Bishop(0,0,colors[0]), 
"B":Bishop(0,0,colors[1]), "r" : Rook(0,0,colors[0]), "R" : Rook(0,0,colors[1]), "n" : Knight(0,0,colors[0]), "N" : Knight(0,0,colors[1]), 
"p" : Pawn(0,0,colors[0]), "P" : Pawn(0,0,colors[1])}


def isWhite(x,y):
    return (x%2 + y%2)%2 == 0

def drawSquare(x,y,scale,w,b,screen):
    cell = pygame.Rect(x*scale,y*scale,scale,scale)
    if(isWhite(x,y)):
        pygame.draw.rect(screen,w,cell)
    else:
        pygame.draw.rect(screen,b,cell)


def drawLine(window,x,y,color1,color2):
    for i in range(8):
        cell = pygame.Rect(x,y,cellScale,cellScale)
        if(i%2):
            pygame.draw.rect(window,color2,cell)
        else:
            pygame.draw.rect(window,color1,cell)
        x+=cellScale

def  drawBoard(window):
    yCount = 0
    xCount = 0
    for i in range(8):
        if(i%2):
            drawLine(window,xCount,yCount,black,white)
            yCount += cellScale
        else:
            drawLine(window,xCount,yCount,white,black)
            yCount += cellScale


def display(window,scale,pieces):
    for piece in pieces.values():
        piece.display(window,scale)

def convertStringInBoard(board,string):
        x = 0
        y = 0
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
                    board.pieces[x*8+y] = copy.copy(pieces[char])
                    if type(pieces[char]) == type(King(0,0,"w")):
                        board.kings.append(board.pieces[x*8+y])
                    x+=1

def update(window,scale,pieces):
    drawBoard(window)
    display(window,scale,pieces)


def displayMoves(piece,scale,board,screen):
    piece.getPossibleMoves(board)
    img = pygame.image.load(r'sprites/moves.png')
    img = pygame.transform.scale(img, (scale,scale))
    for move in piece.getPossibleMoves(board):
        screen.blit(img,(move.to[0]*scale,move.to[1]*scale))