import copy
from moves import Move
columns = ["a","b","c","d","e","f","g","h"]

class Chessboard:

    def registerMove(self,before,piece,length):
        if(len(self.pieces) != length):
            eated = self.eaten[-1]
            self.moves.append(str(before) + columns[before.y] + str(abs(before.y-8)) +"x" + str(eated) + columns[eated.x] + str(abs(eated.y-8))) 
        else:
            self.moves.append(str(piece) + columns[piece.x] + str(abs(piece.y-8))) 

    def outOfBounds(self,x,y):
        return x>self.maxX or x<0 or y>self.maxY or y<0
        
    def getPiece(self,x,y):
        index = x*8 + y
        return self.pieces.get(index,0)
        

    def changePositionOf(self,piece,x,y):
        self.pieces[x*8+y] = copy.deepcopy(piece)

        if type(piece) == type(self.turnKing()):
            self.kings[(self.turn+1)%2] = self.pieces[x*8+y]

        del self.pieces[piece.x*8+piece.y]
        self.pieces[x*8+y].x = x
        self.pieces[x*8+y].y = y
        self.pieces[x*8+y].moved += 1

            

    def pat(self):
        return self.checkmate() == 1 

    def checkmate(self):
        res = True
        #print(self.turn)
        for piece in self.pieces.values():
            if piece.color == self.turnColor():
                moves = piece.getPossibleMoves(self)
                if len(moves):
                    #print(piece.moves[-1])
                    res = False                       
        return res
                        
    def check(self):
        king = self.turnKing()
        return king.somethingInTheWay(king.x,king.y,self)


    def nexTurn(self,piece,x,y):
        if(piece.move(x,y,self)):
            self.turn += 1
            print(self.moves[-1])
            if self.checkmate():
                if self.check():
                    print("checkmate")
                    return -2
                print("pat")
                return -1

            elif self.check():
                print("check")

            return 1
        return 0


    def turnColor(self):
        return self.colors[self.turn%2]

    def turnKing(self):
        return self.kings[(self.turn+1)%2]

    def copyTo(self,other):
        other.turn = copy.copy(self.turn)
        other.kings = copy.deepcopy(self.kings)
        other.moves = copy.deepcopy(self.moves)
        other.pieces = copy.deepcopy(self.pieces)


    def __init__(self):
        self.colors = ["white","black"]
        self.turn = 0
        self.kings = []
        self.pieces = {}
        self.moves = []
        self.maxX = 8
        self.maxY = 8

    #reverse display: you need just to substract by the size of height for y and width for x and get their absolute value to reverse the positions

    #Pour vérifier si il y echec et mat il faut vérifier tous les coups possible et si aucun ne permet d'empĉher l'echec et mat