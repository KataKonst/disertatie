from flask import Blueprint, request
from mongo.gameService import GameService
from bson.json_util import dumps

games = Blueprint('games', __name__, template_folder='web')
gameService = GameService()
##gameService.processForGame("Arma3")


@games.route('/add', methods=['POST'])
def add():
    gameService.add(request.get_json())
    return "succes"


@games.route('/all/')
def getAll():
    res = gameService.all()
    return dumps(res)


@games.route('/name/<name>/page/<page>/size/<size>')
def searchByName(name, page, size):
    res = dict({'length': gameService.countReviewsByGame(name),
                'results': gameService.findByName(name, int(page), int(size))})
    return dumps(res)


@games.route('/average/page/<page>/size/<size>/alg/<algorithm>')
def averrage(page, size, algorithm):

    if algorithm == 'vader':
        results = gameService.averrageByVader(int(page), int(size))
        return dumps(dict({'length': results[0]['metadata'][0]['total'],
                           'results': results[0]['data']}))

    if algorithm == 'stanford':
        results = gameService.averrageByStanford(int(page), int(size))
        return dumps(dict({'length':results[0]['metadata'][0]['total'],
                'results': results[0]['data']}))

    if algorithm == 'bayes':
        results = gameService.averrageByBayes(int(page), int(size))
        return dumps(dict({'length': results[0]['metadata'][0]['total'],
                           'results': results[0]['data']}))

    if algorithm == 'svm':
        results = gameService.averrageBySvm(int(page), int(size))
        return dumps(dict({'length': results[0]['metadata'][0]['total'],
                           'results': results[0]['data']}))


    return ""