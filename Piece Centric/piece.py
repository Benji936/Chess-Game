from abc import abstractmethod

class Piece:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color
    
    def move(self,x,y):
        if self.isLegalmove(x,y):
            self.x = x
            self.y = y
        else:
            print("Illegal Move")
    
    @abstractmethod
    def canMoveTo(self,x,y):
        pass