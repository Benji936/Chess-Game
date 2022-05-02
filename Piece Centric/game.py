from bishop import Bishop
from piece import Piece
from chessboard import Chessboard

import sys, pygame
from pygame.locals import *

white = (255,249,201)
selected_white = (255,215,162)
black = (114,162,86)
selected_black = (165,223,121)
scale = 800
size = scale, scale
cellScale = int(scale/8)


pygame.init()
screen = pygame.display.set_mode(size)


def isWhite(x,y):
    return (x%2 + y%2)%2 == 0

def loadImages(board):
    for piece in board.pieces:
        piece.loadImage(board.scale)

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




def movePiece(piece,x,y):
    drawSquare(piece.x,piece.y,cellScale,white,black)
    if(piece.move(x,y,game)):
        drawSquare(x,y,cellScale,white,black)
    piece.display(screen,game.scale)


game = Chessboard(cellScale,"RNBKQBNR/PPPPPPPP/////pppppppp/rnbkqbnr")
loadImages(game)
drawBoard()
game.display(screen)

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
                movePiece(select,pos1,pos2)
                pieceSelected = 0
            
                select = None
            else:
                select = game.getPiece(pos1,pos2)
                if select:
                    drawSquare(pos1,pos2,cellScale,selected_white,selected_black)
                    select.display(screen,game.scale)
                    if(select != 0): pieceSelected = 1



    pygame.display.flip()
    
