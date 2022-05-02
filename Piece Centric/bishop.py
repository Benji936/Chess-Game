import pygame
from piece import Piece

class Bishop(Piece):
    def canMoveTo(self,x,y):
        return (abs(self.x-x) - abs(self.y-y) == 0)

    def somethingInTheWay(self,x,y,board):
        if(self.x == x and self.y == y): 
            return 1
        x_mov = (x-self.x) / abs(x-self.x) 
        y_mov = (y-self.y) / abs(y-self.y) 
        i = 1
        while(self.x + i*x_mov != x and self.y + i*y_mov != y):
            piece = board.getPiece(self.x + i*x_mov,self.y + i*y_mov)
            if piece:
                return 1
            i+=1

        
        

    def loadImage(self,scale):
        img = pygame.image.load(r'sprites/'+ self.color +'_bishop.png')
        img = pygame.transform.scale(img, (scale,scale))
        self.image = img
    

            