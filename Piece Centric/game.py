from pprint import pprint
from chessboard import Chessboard
from IA import ia
from utils import *
import sys
import time



if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode(size)
    icon = pieces["n"].loadImage(cellScale)
    pygame.display.set_icon(icon)

    game = Chessboard()
    #convertStringInBoard(game,"K/7r/6r/////k")
    

    convertStringInBoard(game,"RNBQKBNR/PPPPPPPP/////pppppppp/rnbqkbnr")  
    #update(screen,cellScale,game.pieces)

    pieceSelected = 0
    select = game.getPiece(0,0)

    while 1:

        move = ia(game,0,2,0)[1]
        print(move)
        if move:
            move.applyMove(game)
            game.turn += 1
            if game.checkEverything() < 0:
                exit()

        update

        #for event in pygame.event.get():

            #if event.type == pygame.QUIT: sys.exit()

        """if event.type == pygame.MOUSEBUTTONUP and game.turnColor() == "white":
                
                pos = pygame.mouse.get_pos()

                #Scaling the position 
                pos1 = int(pos[0]/cellScale)
                pos2 = int(pos[1]/cellScale)

                if pieceSelected:
                    try:
                        promotions = select.canPromote(pos1,pos2)
                        if promotions and select.canMoveTo(pos1,pos2,game):
                            index = int(input("Wich promotions do you want ? "))

                        #Moves the piece and change turn
                        if game.nexTurn(select,pos1,pos2,promotions[index]) < 0:
                            exit()
                    except Exception as e:
                        #print(e)
                        #Moves the piece and change turn
                        if game.nexTurn(select,pos1,pos2) < 0:
                            exit()

                    #Graphic update and reset of selection for the next player
                    update(screen,cellScale,game.pieces)
                    pieceSelected = 0
                    select = None
                else:
                    select = game.getPiece(pos1,pos2)
                    if select:
                        if select.color == game.turnColor():
                            #Draw the square with a different color to see the selection
                            drawSquare(pos1,pos2,cellScale,selected_white,selected_black,screen)
                            select.display(screen,cellScale)
                            displayMoves(select,cellScale,game,screen)
                            pieceSelected = 1"""

            #if game.turnColor() == "black":

        
                #update(screen,cellScale,game.pieces)
                


        update(screen,cellScale,game.pieces)
        pygame.display.flip()
    
