
from piece import Piece

class Pawn(Piece):
    def canMoveTo(self,x,y):
        return (self.y == y or self.x ==x) or (abs(self.x-x) - abs(self.y-y) == 0)