class Move:
    def __init__(self,piece,pos2):
        self.piece = piece
        self.to = pos2
        self.eatenPiece = None 

    def eats(self,board):
        return board.getPiece(self.to[0],self.to[1])
    
    def applyMove(self,board):
        self.eatenPiece = board.getPiece(self.to[0],self.to[1])
        board.changePositionOf(self.piece,self.to[0],self.to[1])
        board.moves.append(self)


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


class Castle(Move):
    def __init__(self,piece,pos1,rook,pos2):
        self.piece = piece
        self.rook = rook
        self.kingMove = pos1
        self.rookMove = pos2

    def applyMove(self,board):
        board.changePositionOf(self.piece,self.kingMove[0],self.kingMove[1])
        board.changePositionOf(self.rook,self.rookMove[0],self.rookMove[1])
        board.moves.append(self)

class Promote(Move):
    pass