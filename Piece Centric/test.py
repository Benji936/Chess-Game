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

    def test_king(self):
        game = Chessboard()
        game.turn = 7
        convertStringInBoard(game,"R1BQKBNR/PPP11qPP/2NP/4P/2b1p//pppp1ppp/rnb1k1nr")

        move = game.turnKing().canMoveTo(5,1,game) 
        moves = game.turnKing().getPossibleMoves(game)     

        self.assertEqual(len(moves), 0,"king can't move")
        self.assertEqual(move, False,"king try to eat a defended piece")


    def test_queen(self):
        self.assertEqual(2, 2, "Tesseract")

if __name__ == '__main__':
    unittest.main()