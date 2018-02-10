from flask import Blueprint, request
from mongo.gameService import GameService
from bson.json_util import dumps

games = Blueprint('games', __name__, template_folder='web')
gameService = GameService()
gameService.processForGame("Arma3")


@games.route('/add', methods=['POST'])
def add():
    gameService.add(request.get_json())
    return "succes"


@games.route('/all/page/<page>/size/<size>')
def getAll(page,size):
    res = dict({'length': gameService.countGames(),
                'results': gameService.all(int(page), int(size))})
    return dumps(res)


@games.route('/col/<name>/page/<page>/size/<size>')
def searchByName(name, page, size):
    res = dict({'length': gameService.countReviewsByGame(name),
                'results': gameService.findByName(name, int(page), int(size))})
    return dumps(res)
