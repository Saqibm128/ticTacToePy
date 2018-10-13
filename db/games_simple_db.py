from addict import Dict
from random import randint

class SimpleStorage():
    """Holds a very silly way to implement storage until I decide what i wanna actually use"""
    def __init__(self):
        self._data = Dict()
        self.maxId = 0

    """ Generate an identifier and new key for new game data """
    def genKey(self):
        self.maxId += 1
        return (str(self.maxId), str(self.maxId)) #this is simple, so duh

    """ Generate game object from data lookup """
    def getBoard(self, id, key):
        if (key == id):
            return self._data[key]
        elif id not in self._data.keys():
            return {"response": "failed to find game", "error": "true"}
        else:
            return {"response": "incorrect creds", "error": "true"}
    """ Save game object in simple data structure """
    def saveBoard(self, id, key, board):
        if (key == id):
            self._data[key] = board.dict()
