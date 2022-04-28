from piece import Piece

class King(Piece):
   def canMoveTo(self,x,y):
        return (abs(self.y - y) == 1 or abs(self.x -x) == 1)