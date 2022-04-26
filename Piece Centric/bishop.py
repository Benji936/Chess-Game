from piece import Piece

class Bishop(Piece):
    def canMoveTo(self,x,y):
        return (abs(self.x-x) - abs(self.y-y) == 0)
    

            