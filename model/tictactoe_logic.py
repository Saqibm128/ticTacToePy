from enum import Enum


class Tile(Enum):
    X = 'X'
    O = 'O'
    EMPTY = '.'  # Game can still continue
    # Game cannot be continued or is already finished. We assume a full board is this, even if it is already catscratch.
    NO_WIN = '.'

    def winner(self):
        return self

    def isDone(self):
        return self == Tile.X or self == Tile.O

class Winnable:
        def __init__(self, length):
            self.length = length
            self.boards = []
            self.currentPlayer = Tile.X

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

            def changeCurrentPlayer(self):
                self.currentPlayer = Tile.O if Tile.X else Tile.X


class UltimateBoard(Winnable):
    def __init__(self, length=3):
        super().__init__(length)
        self.length = length
        self.boards = []
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

    def play(self, x, y):
        if (self.currentBoard == (-1, -1)):
            raise Exception("Pick 3 by 3 sub-board first!")
        if (self.isDone):
            raise Exception("Game is already finished")
        x_sup, y_sup = self.currentBoard[0], self.currentBoard[1]
        result = self.boards[x_sup][y_sup].play(x, y)
        if result != Tile.EMPTY:
            raise Exception("Board tile is already occupied")
        else:
            self.changeCurrentPlayer()
            self.changeBoards(self.currentPlayer)
            if (self.boards[x][y].isDone):
                self.currentBoard = (-1, -1)
            else:
                self.currentBoard = (x, y)
        self.winner() #updates isdone

    def changeBoards(tile):
        for x in range(length):
            for y in range(length):
                self.boards[x][y].currentPlayer = tile;


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

        for i in range(length):
            self.boards.append([])
            for j in range(length):
                self.boards[i].append(Tile.EMPTY)

    def play(x, y):
        if self.boards[x][y] == Tile.EMPTY:
            self.boards[x][y] = self.currentPlayer
            self.changeCurrentPlayer()
            return Tile.EMPTY
        else:
            return self.boards[x][y]
        self.winner() #updates isdone
