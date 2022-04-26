from abc import abstractmethod


class Piece:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    
    @abstractmethod
    def move(x,y):
        return
    
    @abstractmethod
    def isLegalmove(x,y):
        return