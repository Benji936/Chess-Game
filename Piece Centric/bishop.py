from piece import Piece

class Bishop(Piece):
    def isLegalmove(self,x,y):
        return (abs(self.x-x) - abs(self.y-y) == 0)
    
    def move(self,x,y):
        if self.isLegalmove(x,y):
            self.x = x
            self.y = y
        else:
            print("Illegal Move")
            