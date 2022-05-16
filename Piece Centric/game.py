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
colors = ["white","black"]

pieces = {"k" : King(0,0,colors[0]), "K" : King(0,0,colors[1]), "q" : Queen(0,0,colors[0]), "Q" : Queen(0,0,colors[1]), "b" : Bishop(0,0,colors[0]), 
"B":Bishop(0,0,colors[1]), "r" : Rook(0,0,colors[0]), "R" : Rook(0,0,colors[1]), "n" : Knight(0,0,colors[0]), "N" : Knight(0,0,colors[1]), 
"p" : Pawn(0,0,colors[0]), "P" : Pawn(0,0,colors[1])}


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
    convertStringInBoard(game,"RNBQKBNR/PPPPPPPP/////pppppppp/rnbqkbnr")
    loadImages(game,cellScale)
    update(screen,cellScale,game.pieces)

    pieceSelected = 0
    select = game.getPiece(0,0)

    while 1:

        for event in pygame.event.get():

            if event.type == pygame.QUIT: sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                #Scaling the position 
                pos1 = int(pos[0]/cellScale)
                pos2 = int(pos[1]/cellScale)

                if pieceSelected:
                    #Moves the piece and change turn
                    game.nexTurn(select,pos1,pos2)

                    #Graphic update and reset of selection for the next player
                    update(screen,cellScale,game.pieces)
                    pieceSelected = 0
                    select = None
                else:
                    select = game.getPiece(pos1,pos2)
                    if select:
                        if select.color == game.wichColorTurn():
                            #Draw the square with a different color to see the selection
                            drawSquare(pos1,pos2,cellScale,selected_white,selected_black)
                            select.display(screen,cellScale)
                            pieceSelected = 1



        pygame.display.flip()
    
