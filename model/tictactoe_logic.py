from enum import Enum


class Tile(Enum):
    X = 'X'
    O = 'O'
    EMPTY = '.'  # Game can still continue
    # Game cannot be continued or is already finished. We assume a full board is this, even if it is already catscratch.
    NO_WIN = '.'

    def winner(self):
        return self

class Winnable:
        def __init__(self, length):
            self.length = length
            self.boards = []

        def winner(self):
            # did we win horizontally?
            for i in range(self.length):
                maybeWinner = self.boards[i][0].winner()
                for j in range(self.length):
                    if self.boards[i][j].winner() != maybeWinner or self.boards[i][j].winner() == Tile.EMPTY:
                        maybeWinner = Tile.EMPTY
                if maybeWinner != Tile.EMPTY or maybeWinner != Tile.NO_WIN:
                    self.isDone = True
                    return maybeWinner
            # did we win vertically?
            for j in range(self.length):
                maybeWinner = self.boards[0][j].winner()
                for i in range(self.length):
                    if self.boards[i][j].winner() != maybeWinner or self.boards[i][j].winner() == Tile.EMPTY:
                        maybeWinner = Tile.EMPTY
                if maybeWinner != Tile.EMPTY or maybeWinner != Tile.NO_WIN:
                    self.isDone = True
                    return maybeWinner

            # did we win diagonally left to right
            maybeWinner = self.boards[0][0].winner()
            for i in range(self.length):
                maybeWinner = self.boards[0][0]
                if self.boards[i][i].winner() != maybeWinner or self.boards[i][i].winner() == Tile.EMPTY:
                    maybeWinner = Tile.EMPTY
            if maybeWinner != Tile.EMPTY or maybeWinner != Tile.NO_WIN:
                self.isDone = True
                return maybeWinner

            # did we win diagonally right to left
            maybeWinner = self.boards[self.length - 1][0].winner()
            for i in range(self.length):
                maybeWinner = self.boards[self.length - 1][0]
                if self.boards[self.length - i - 1][i].winner() != maybeWinner or self.boards[self.length - i - 1][i].winner() == Tile.EMPTY:
                    maybeWinner = Tile.EMPTY
            if maybeWinner != Tile.EMPTY or maybeWinner != Tile.NO_WIN:
                self.isDone = True
            return maybeWinner




class UltimateBoard(Winnable):
    def __init__(self, length=3):
        super().__init__(length)
        self.length = length
        self.boards = []
        self.currentPlayer = Tile.X
        self.currentBoard = (-1, -1)  # If -1, -1 then any board is possible (player needs to choose)
        self.isDone = False

        for i in range(length):
            self.boards.append([])
            for j in range(length):
                self.boards[i].append(Board(length))

    """
    If first move or we end up going to board which goes to complete board, return true
    """
    def needToPickNextBoard(self):
        return self.currentBoard == (-1,-1)


    """
    Will only work if we can choose a board, otherwise we get back an error
    newBoard should be a tuple
    TODO: validate newBoard is correct tuple type
    """
    def chooseBoard(self, newBoard):
        if not self.needToPickNextBoard():
            raise Exception("Should not pick a new board!")
        else:
            self.currentBoard = newBoard

class Board(Winnable):
    def __init__(self, length=3):
        super().__init__(length)
        self.length = length
        self.boards = []
        self.isDone = False
        self.currentPlayer = Tile.X

        for i in range(length):
            self.boards.append([])
            for j in range(length):
                self.boards[i].append(Tile.EMPTY)
