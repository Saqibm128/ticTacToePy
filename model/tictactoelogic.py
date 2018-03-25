from enum import Enum

class Tile(Enum):
    X = 'X'
    Y = 'Y'
    EMPTY = '.'
    NO_WIN = '.'

class UltimateBoard:
    def __init__(self, length=3):
        self.length = length
        self.boards = []

        for i in range(length):
            self.boards.append([])
            for j in range(length):
                self.boards[i].append(Board(length))
    def isDone(self):
        self.winner() != '.'

    def winner(self):
        #did we win horizontally?
        for i in range(self.length):
            maybeWinner = self.boards[i][0].winner()
            for j in range(self.length):
                if self.boards[i][j].winner() != maybeWinner or self.boards[i][j].winner() == Tile.EMPTY:
                    return Tile.EMPTY
        #did we win vertically?
        for j in range(self.length):
            maybeWinner = self.boards[j][0].winner()
            for i in range(self.length):
                if self.boards[i][j].winner() != maybeWinner or self.boards[i][j].winner() == Tile.EMPTY:
                    return Tile.EMPTY
        #did we win diagonally
        for i in range(self.length):
            maybeWinner = self.boards

class Board:
    def __init__(self, length=3):
        self.length = length
        self.tiles = []

        for i in range(length):
            self.boards.append([])
            for j in range(length):
                self.boards[i].append('.')
