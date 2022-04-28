from bishop import Bishop
from piece import Piece
from chessboard import Chessboard

import sys, pygame
from pygame.locals import *

white = (255,255,255)
black = (255,100,100)
scale = 800
size = scale, scale
cellScale = int(scale/8)


pygame.init()
screen = pygame.display.set_mode(size)


def drawLine(x,y,color1,color2):
    for i in range(8):
        cell = pygame.Rect(x,y,cellScale,cellScale)
        if(i%2):
            pygame.draw.rect(screen,color2,cell)
        else:
            pygame.draw.rect(screen,color1,cell)
        x+=cellScale

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
game.display(screen)
"""image = pygame.image.load(r'sprites/white_king.png')
image = pygame.transform.scale(image, (cellScale,cellScale))
screen.blit(image, (0, 0))"""

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

    pygame.display.flip()

"""bishop = Bishop(4,5)
bishop.move(6,5)
bishop.move(5,6)
bishop.move(6,5)"""