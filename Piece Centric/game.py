from bishop import Bishop
from piece import Piece
from chessboard import Chessboard

import sys, pygame
from pygame.locals import *

white = (255,255,255)
black = (0,200,0)
scale = 800
size = scale, scale
cellScale = int(scale/8)


pygame.init()
screen = pygame.display.set_mode(size)


def isWhite(x,y):
    return (x%2 + y%2)%2 == 0

def drawSquare(x,y,scale):
    cell = pygame.Rect(x*scale,y*scale,scale,scale)
    if(isWhite(x,y)):
        pygame.draw.rect(screen,white,cell)
    else:
        pygame.draw.rect(screen,black,cell)


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






game = Chessboard(cellScale,"rnbkqbnr/pppppppp/////PPPPPPPP/RNBKQBNR")
drawBoard()
game.display(screen)


while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pos1 = int(pos[0]/cellScale)
            pos2 = int(pos[1]/cellScale)

            drawSquare(game.pieces[0].x,game.pieces[0].y,cellScale)
            if(game.pieces[0].move(pos1,pos2)):
                drawSquare(pos1,pos2,cellScale)
            game.pieces[0].display(screen,game.scale)

            
            

    
    pygame.display.flip()
    
