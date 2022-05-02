import pygame
import copy





class Chessboard:
        
    def getPiece(self,x,y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
        return 0


    def __init__(self):
        #Peut être plutot utilisé un Set qu'une liste
        #Ou alors un dictionnaire avec l'indice du tableau
        self.pieces = []

    




    #reverse display: you need just to substract by the size of height for y and width for x and get their absolute value to reverse the positions