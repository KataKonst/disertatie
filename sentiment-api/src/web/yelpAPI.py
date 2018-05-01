from flask import Blueprint
from mongo.yelpService import YelpService
from bson.json_util import dumps

yelp = Blueprint('yelp', __name__, template_folder='web')
yelpService = YelpService()

@yelp.route('/name/<name>/page/<page>/size/<size>')
def searchByName(name, page, size):
    res = dict({'length': yelpService.countReviewsByName(name),
                'results': yelpService.findByName(name, int(page), int(size))})
    return dumps(res)

@yelp.route('/average/page/<page>/size/<size>/alg/<algorithm>')
def averrage(page, size, algorithm):

    if algorithm == 'vader':
        results = yelpService.averrageByVader(int(page), int(size))
        return dumps(dict({'length': results[0]['metadata'][0]['total'],
                           'results': results[0]['data']}))

    if algorithm == 'stanford':
        results = yelpService.averrageByStanford(int(page), int(size))
        return dumps(dict({'length':results[0]['metadata'][0]['total'],
                'results': results[0]['data']}))

    if algorithm == 'bayes':
        results = yelpService.averrageByBayes(int(page), int(size))
        return dumps(dict({'length': results[0]['metadata'][0]['total'],
                           'results': results[0]['data']}))

    if algorithm == 'svm':
        results = yelpService.averrageBySvm(int(page), int(size))
        return dumps(dict({'length': results[0]['metadata'][0]['total'],
                           'results': results[0]['data']}))
    return "not implemented"