import unittest
from tictactoe_logic import Board, UltimateBoard, Tile

class TestTicTacToeLogic(unittest.TestCase):

    noWin = Board()
    noWin.boards[0][0] = Tile.X
    noWin.boards[0][1] = Tile.X
    noWin.boards[0][2] = Tile.O

    verticalWin = Board()
    verticalWin.boards[0][0] = Tile.X
    verticalWin.boards[0][1] = Tile.X
    verticalWin.boards[0][2] = Tile.X

    horizontalWin = Board()
    horizontalWin.boards[0][1] = Tile.X
    horizontalWin.boards[1][1] = Tile.X
    horizontalWin.boards[2][1] = Tile.X

    diagonalWin = Board()
    diagonalWin.boards[0][0] = Tile.X
    diagonalWin.boards[1][1] = Tile.X
    diagonalWin.boards[2][2] = Tile.X

    otherDiagonalWin = Board()
    otherDiagonalWin.boards[2][0] = Tile.O
    otherDiagonalWin.boards[1][1] = Tile.O
    otherDiagonalWin.boards[0][2] = Tile.O

    ultimate = UltimateBoard()
    ultimate.boards[0][0] = horizontalWin
    ultimate.boards[0][1] = verticalWin
    ultimate.boards[0][2] = diagonalWin


    def testTicTacToe_no_boardWin(self):
        board = self.noWin
        self.assertEqual(board.winner(), Tile.EMPTY)
        self.assertFalse(board.isDone)

    def testTicTacToe_vertical_boardWin(self):
        board = self.verticalWin
        self.assertEqual(board.winner(), Tile.X)
        self.assertTrue(board.isDone)

    def testTicTacToe_horizontal_boardWin(self):
        board = self.horizontalWin
        self.assertEqual(board.winner(), Tile.X)
        self.assertTrue(board.isDone)

    def testTicTacToe_diagonalWin(self):
        board = self.diagonalWin
        self.assertEqual(board.winner(), Tile.X)
        self.assertTrue(board.isDone)

    def testTicTacToe_other_diagonalWin(self):
        board = self.otherDiagonalWin
        self.assertEqual(board.winner(), Tile.O)
        self.assertTrue(board.isDone)

    def test_ultimate_ticTacToeWin(self):
        board = self.ultimate
        self.assertEqual(board.winner(), Tile.X)
        self.assertTrue(board.isDone)


if __name__ == '__main__':
    unittest.main()
