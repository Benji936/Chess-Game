from abc import abstractmethod


class Piece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    @abstractmethod
    def move(self,x,y):
        pass
    
    @abstractmethod
    def isLegalmove(self,x,y):
        pass