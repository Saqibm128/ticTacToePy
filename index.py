from flask import Flask, request
from db.games_simple_db import SimpleStorage
from model.tictactoe_logic import UltimateBoard
import json
app = Flask(__name__)

storage = SimpleStorage();

@app.route("/", methods=["GET"])
def status():
    return "OK";

@app.route("/", methods=["OPTIONS"])
def options():
    return json.dumps({
        "New Game": {
            "method" : "GET",
            "path" : "/game/new"
        },
        "Get Game": {
            "method" : "POST",
            "path" : "/game"
        },
    })

@app.route("/game", methods=["POST"])
def getGame():
    if not "gameID" in request.form.keys() or not "gameKey" in request.form.keys():
        return json.dumps({"response": "need gameID or gameKey in request", \
                           "error": "true"})
    return json.dumps(storage.getBoard(request.form["gameID"], request.form["gameKey"]));

@app.route("/game/new", methods=["GET"])
def newGame():
    board = UltimateBoard()
    keyPair = storage.genKey()
    storage.saveBoard(str(keyPair[0]), str(keyPair[1]), board)
    return json.dumps({"id": str(keyPair[0]), "key": str(keyPair[1])})

@app.route("/game/play", methods=["POST"])
def play():
    if not "gameID" in request.form.keys() or not "gameKey" in request.form.keys():
        return json.dumps({"response": "need gameID or gameKey in request", \
                           "error": "true"})
    boardDict = storage.getBoard(request.form["gameID"], request.form["gameKey"]);
    if "error" in board.keys():
        return json.dumps(boardDict)

def boardFromDict():
    board = UltimateBoard()


if __name__ == "__main__":
    app.run(debug=True, port=8080)
