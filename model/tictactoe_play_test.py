import unittest
from tictactoe_logic import Board, UltimateBoard, Tile

class TestTicTacToePlay(unittest.TestCase):



    def test_ticTacToe_X_win(self):
        board = Board()
        self.assertEqual(board.currentPlayer, Tile.X)
        board.play(1, 1)
        self.assertEqual(board.currentPlayer, Tile.O)
        board.play(0, 0)
        self.assertEqual(board.currentPlayer, Tile.X)
        board.play(0, 1)
        self.assertEqual(board.currentPlayer, Tile.O)
        board.play(1, 2)
        self.assertEqual(board.currentPlayer, Tile.X)
        board.play(2, 1)
        self.assertEqual(board.currentPlayer, Tile.O)
        self.assertTrue(board.isDone)
        self.assertEqual(board.winner(), Tile.X)
        self.assertEqual(board.currentPlayer, Tile.O)
        with self.assertRaises(Exception) as case:
            board.play(1,0)
    def test_noWin(self):
        board = Board()
        self.assertEqual(board.currentPlayer, Tile.X)
        board.play(1, 1)
        self.assertEqual(board.currentPlayer, Tile.O)
        board.play(0, 0)
        self.assertEqual(board.currentPlayer, Tile.X)
        board.play(0, 1)
        self.assertEqual(board.currentPlayer, Tile.O)
        board.play(2, 1)
        self.assertEqual(board.currentPlayer, Tile.X)
        board.play(0, 2)
        self.assertEqual(board.currentPlayer, Tile.O)
        board.play(2, 0)
        self.assertEqual(board.currentPlayer, Tile.X)
        board.play(1, 0)
        self.assertEqual(board.currentPlayer, Tile.O)
        board.play(1, 2)
        self.assertEqual(board.currentPlayer, Tile.X)
        board.play(2, 2)
        self.assertEqual(board.winner(), Tile.NO_WIN)
        self.assertTrue(board.isDone)



if __name__ == '__main__':
    unittest.main()
