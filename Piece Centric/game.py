from king import King
from queen import Queen
from bishop import Bishop
from rook import Rook
from knight import Knight
from pawn import Pawn
from piece import Piece
from chessboard import Chessboard

import copy
import sys, pygame
from pygame.locals import *

white = (255,249,201)
selected_white = (255,215,162)
black = (114,162,86)
selected_black = (165,223,121)
initScale = 800
size = initScale, initScale
cellScale = int(initScale/8)

pieces = {"k" : King(0,0,"white"), "K" : King(0,0,"black"), "q" : Queen(0,0,"white"), "Q" : Queen(0,0,"black"), "b" : Bishop(0,0,"white"), 
"B":Bishop(0,0,"black"), "r" : Rook(0,0,"white"), "R" : Rook(0,0,"black"), "n" : Knight(0,0,"white"), "N" : Knight(0,0,"black"), 
"p" : Pawn(0,0,"white"), "P" : Pawn(0,0,"black")}


def isWhite(x,y):
    return (x%2 + y%2)%2 == 0

def loadImages(board,scale):
    for piece in board.pieces.values():
        piece.loadImage(scale)

def drawSquare(x,y,scale,w,b):
    cell = pygame.Rect(x*scale,y*scale,scale,scale)
    if(isWhite(x,y)):
        pygame.draw.rect(screen,w,cell)
    else:
        pygame.draw.rect(screen,b,cell)


def drawLine(x,y,color1,color2):
    for i in range(8):
        cell = pygame.Rect(x,y,cellScale,cellScale)
        if(i%2):
            pygame.draw.rect(screen,color2,cell)
        else:
            pygame.draw.rect(screen,color1,cell)
        x+=cellScale



def  drawBoard():
    yCount = 0
    xCount = 0
    for i in range(8):
        if(i%2):
            drawLine(xCount,yCount,black,white)
            yCount += cellScale
        else:
            drawLine(xCount,yCount,white,black)
            yCount += cellScale


def display(screen,scale,pieces):
    for piece in pieces.values():
        piece.display(screen,scale)
        #screen.blit(piece.image,(piece.x*scale,piece.y*scale))

def convertStringInBoard(board,string):
        x = 0
        y = 0
        board.pieces = {}
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
                    x+=1


def movePiece(piece,x,y,board):
    drawSquare(piece.x,piece.y,cellScale,white,black)
    if(piece.move(x,y,game)):
        drawSquare(x,y,cellScale,white,black)
        board.getPiece(x,y).display(screen,cellScale)
    else:
        piece.display(screen,cellScale)

def update(screen,scale,pieces):
    drawBoard()
    display(screen,scale,pieces)





if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode(size)

    game = Chessboard()
    convertStringInBoard(game,"RNBKQBNR/PPPPPPPP/////pppppppp/rnbkqbnr")
    loadImages(game,cellScale)
    update(screen,cellScale,game.pieces)

    pieceSelected = 0
    select = game.getPiece(0,0)


    while 1:

        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                pos1 = int(pos[0]/cellScale)
                pos2 = int(pos[1]/cellScale)

                if pieceSelected:
                    #movePiece(select,pos1,pos2,game)
                    select.move(pos1,pos2,game)
                    update(screen,cellScale,game.pieces)
                    pieceSelected = 0
                    select = None
                else:
                    select = game.getPiece(pos1,pos2)
                    if select:
                        drawSquare(pos1,pos2,cellScale,selected_white,selected_black)
                        select.display(screen,cellScale)
                        pieceSelected = 1



        pygame.display.flip()
    
