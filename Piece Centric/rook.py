from piece import Piece

class Rook(Piece):
    def canMoveTo(self,x,y):
        return (self.y == y or self.x ==x)