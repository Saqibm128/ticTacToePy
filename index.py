from flask import Flask, request
from db.games_simple_db import SimpleStorage
from model.tictactoe_logic import UltimateBoard
import json
app = Flask(__name__)

storage = SimpleStorage();

@app.route("/")
def status():
    return "OK";

@app.route("/game", methods=["POST"])
def getGame():
    if not "gameID" in request.form.keys() or not "gameKey" in request.form.keys():
        return json.dumps({"response": "need gameID or gameKey in request", \
                           "error": "true"})
    return json.dumps(storage.getBoard(request.form["gameID"], request.form["gameKey"]));

@app.route("/new", methods=["GET"])
def newGame():
    board = UltimateBoard()
    keyPair = storage.genKey()
    storage.saveBoard(keyPair[0], keyPair[1], board)
