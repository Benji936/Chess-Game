import copy

class Chessboard:

    def outOfBounds(self,x,y):
        return x>self.maxX or x<0 or y>self.maxY or y<0
        
    def getPiece(self,x,y):
        index = x*8 + y
        return self.pieces.get(index,0)
        

    def changePositionOf(self,piece,x,y):
        self.pieces[x*8+y] = copy.copy(piece)
        del self.pieces[piece.x*8+piece.y]
        self.pieces[x*8+y].x = x
        self.pieces[x*8+y].y = y
        self.pieces[x*8+y].moved += 1

    def pat(self):
        return self.checkmate() == 1 

    def checkmate(self):
        count = 0
        king = self.kings[(self.turn+1)%2]
        for i in range(-1,2):
            for j in range(-1,2):
                count += king.canMoveTo(king.x+i,king.y+j,self)
        check = not self.check()
        return count + check


    def check(self):
        king = self.kings[(self.turn+1)%2]
        return king.somethingInTheWay(king.x,king.y,self)


    def nexTurn(self,piece,x,y):
        if(piece.move(x,y,self)):
            self.turn += 1
            if self.checkmate() == 0 or self.pat():
                return 0
            return 1
        return 0


    def wichColorTurn(self):
        return self.colors[self.turn%2]

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