from flask import Blueprint
from mongo.tweetService import TweetService
from bson.json_util import dumps

tweets = Blueprint('tweet', __name__, template_folder='web')
tweetService = TweetService()

@tweets.route('/location/<location>/page/<page>/size/<size>')
def searchByLocation(location, page, size):
    res = dict({'length' :tweetService.countByLocation(location),
                'results': tweetService.findByLocation(location, int(page), int(size))})
    return dumps(res)

@tweets.route('/location-full/<location>/page/<page>/size/<size>')
def searchByLocationFullName(location, page, size):
    res = dict({'length' :tweetService.countByLocationFullName(location),
                'results': tweetService.findByLocationFullName(location, int(page), int(size))})
    return dumps(res)

@tweets.route('/average/page/<page>/size/<size>/alg/<algorithm>')
def averrage(page, size, algorithm):

    if algorithm == 'vader':
        results = tweetService.averrageByLocation(int(page), int(size))
        return dumps(dict({'length': results[0]['metadata'][0]['total'],
                           'results': results[0]['data']}))

    if algorithm == 'stanford':
        results = tweetService.averrageByLocationStanford(int(page), int(size))
        return dumps(dict({'length':results[0]['metadata'][0]['total'],
                'results': results[0]['data']}))

    if algorithm == 'svm':
        results = tweetService.averrageByLocationSvm(int(page), int(size))
        return dumps(dict({'length':results[0]['metadata'][0]['total'],
                'results': results[0]['data']}))

    if algorithm == 'bayes':
        results = tweetService.averrageByLocationBayes(int(page), int(size))
        return dumps(dict({'length':results[0]['metadata'][0]['total'],
                'results': results[0]['data']}))

    return ""
