columns = ["a","b","c","d","e","f","g","h"]

class Move:
    def __init__(self,piece,pos):
        self.piece = piece
        self.to = pos
        self.eatenPiece = None 

    def eats(self,board):
        return board.getPiece(self.to[0],self.to[1])
    
    def applyMove(self,board):
        self.eatenPiece = board.getPiece(self.to[0],self.to[1])
        board.changePositionOf(self.piece,self.to[0],self.to[1])
        board.moves.append(self)

    def __str__(self):
        if self.eatenPiece:
            return str(self.piece) + columns[self.piece.x] + str(abs(self.piece.y-8)) + "x" + str(self.eatenPiece) + columns[self.eatenPiece.x] + str(abs(self.eatenPiece.y-8))
        else:
            return str(self.piece) + columns[self.to[0]] + str(abs(self.to[1]-8)) 


class enPassant(Move):
    def __init__(self,piece,pos,eatPos):
        self.piece = piece
        self.to = pos
        self.eatPos = eatPos
        self.eatenPiece = None

    def applyMove(self,board):
        self.eatenPiece =  board.getPiece(self.eatPos[0],self.eatPos[1])
        board.changePositionOf(self.piece,self.to[0],self.to[1])
        del board.pieces[self.eatPos[0]*8+self.eatPos[1]]
        board.moves.append(self)

    def __str__(self):
        return str(self.piece) + columns[self.piece.x] + str(abs(self.piece.y-8)) + "x" + str(self.eatenPiece) + columns[self.eatenPiece.x] + str(abs(self.eatenPiece.y-8)) + " e.p"


class Castle(Move):
    def __init__(self,piece,pos1,rook,pos2):
        self.piece = piece
        self.rook = rook
        self.to = pos1
        self.rookMove = pos2

    def applyMove(self,board):
        board.changePositionOf(self.piece,self.to[0],self.to[1])
        board.changePositionOf(self.rook,self.rookMove[0],self.rookMove[1])
        board.moves.append(self)

    def __str__(self):
        if self.to[0] < 4:
            return "O-O-O"
        else:
            return "O-O"

class Promote(Move):
    def __init__(self,piece,promote,pos):
        self.piece = piece
        self.promotion = promote
        self.to = pos
        self.eatenPiece = None 

    def applyMove(self,board):
        self.eatenPiece = board.getPiece(self.to[0],self.to[1])
        board.changePositionOf(self.promotion,self.to[0],self.to[1])
        board.moves.append(self)

    def __str__(self):
        return super().__str__() + " = " + str(self.promotion)
