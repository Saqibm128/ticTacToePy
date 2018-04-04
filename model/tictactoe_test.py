import unittest
from tictactoelogic import Board, UltimateBoard, Tile

class TestTicTacToeLogic(unittest.TestCase):

    no_win = Board()
    no_win.boards[0][0] = Tile.X
    no_win.boards[0][1] = Tile.X
    no_win.boards[0][2] = Tile.O

    vertical_win = Board()
    vertical_win.boards[0][0] = Tile.X
    vertical_win.boards[0][1] = Tile.X
    vertical_win.boards[0][2] = Tile.X

    horizontal_win = Board()
    horizontal_win.boards[0][1] = Tile.X
    horizontal_win.boards[1][1] = Tile.X
    horizontal_win.boards[2][1] = Tile.X

    diagonal_win = Board()
    diagonal_win.boards[0][0] = Tile.X
    diagonal_win.boards[1][1] = Tile.X
    diagonal_win.boards[2][2] = Tile.X

    otherDiagonal_win = Board()
    otherDiagonal_win.boards[2][0] = Tile.O
    otherDiagonal_win.boards[1][1] = Tile.O
    otherDiagonal_win.boards[0][2] = Tile.O

    ultimate = UltimateBoard()
    ultimate.boards[0][0] = horizontal_win
    ultimate.boards[0][1] = vertical_win
    ultimate.boards[0][2] = diagonal_win


    def test_ticTacToe_no_board_win(self):
        board = self.no_win
        self.assertEqual(board.winner(), Tile.EMPTY)
        self.assertFalse(board.isDone)

    def test_ticTacToe_vertical_board_win(self):
        board = self.vertical_win
        self.assertEqual(board.winner(), Tile.X)
        self.assertTrue(board.isDone)

    def test_ticTacToe_horizontal_board_win(self):
        board = self.horizontal_win
        self.assertEqual(board.winner(), Tile.X)
        self.assertTrue(board.isDone)

    def test_ticTacToe_diagonal_win(self):
        board = self.diagonal_win
        self.assertEqual(board.winner(), Tile.X)
        self.assertTrue(board.isDone)

    def test_ticTacToe_other_diagonal_win(self):
        board = self.otherDiagonal_win
        self.assertEqual(board.winner(), Tile.O)
        self.assertTrue(board.isDone)

    def test_ultimate_ticTacToe_win(self):
        board = self.ultimate
        self.assertEqual(board.winner(), Tile.X)
        self.assertTrue(board.isDone)


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
