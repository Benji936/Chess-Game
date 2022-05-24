import unittest
from piece import Piece
from king import King
from queen import Queen
from knight import Knight
from bishop import Bishop
from pawn import Pawn
from rook import Rook
from chessboard import Chessboard
from game import convertStringInBoard




class TestPieces(unittest.TestCase):

    def test_checkmate_by_rooks(self):
        game = Chessboard()
        convertStringInBoard(game,"K/7r/6r/////k")

        move = game.getPiece(6,2).move(6,0,game)  
        game.turn += 1 
        check = game.check()
        checkmate = game.checkmate()

        self.assertEqual(move, True,"Rook moves")
        self.assertEqual(check, True,"Check")
        self.assertEqual(checkmate, True,"Checkmate")

    def test_checkmate_by_defended_queen(self):
        game = Chessboard()

        convertStringInBoard(game,"2K/RPP/2q/7P/P2Ppb//pp2Bppp/r3r1k")
        game.kings[0].moved += 1
        game.kings[1].moved += 1

        move = game.getPiece(2,2).move(2,1,game) 
        game.turn += 1 
        check = game.check()
        checkmate = game.checkmate() 

        self.assertEqual(move, True,"Rook moves")
        self.assertEqual(check, True,"Check")
        self.assertEqual(checkmate, True,"Checkmate")


    def test_queen(self):
        self.assertEqual(2, 2, "Tesseract")

if __name__ == '__main__':
    unittest.main()