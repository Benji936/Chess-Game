from bishop import Bishop
from piece import Piece

import sys, pygame
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)
size = width, height = 500, 500
cellWidth = int(width/8)
cellHeight = int(height/8)

pygame.init()
screen = pygame.display.set_mode(size)


def drawLine(x,y,color1,color2):
    for i in range(8):
        cell = pygame.Rect(x,y,cellWidth,cellHeight)
        if(i%2):
            pygame.draw.rect(screen,color2,cell)
        else:
            pygame.draw.rect(screen,color1,cell)
        x+=cellWidth

yCount = 0
xCount = 0
for i in range(8):
    if(i%2):
        drawLine(xCount,yCount,black,white)
        yCount += cellHeight
    else:
        drawLine(xCount,yCount,white,black)
        yCount += cellHeight

while 1:

    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

    pygame.display.flip()

"""bishop = Bishop(4,5)
bishop.move(6,5)
bishop.move(5,6)
bishop.move(6,5)"""