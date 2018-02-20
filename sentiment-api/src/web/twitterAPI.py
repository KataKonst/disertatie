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

@tweets.route('/average/page/<page>/size/<size>')
def averrage(page, size):
    res = dict({'length':tweetService.averrageByLocationCount(),
                'results': tweetService.averrageByLocation(int(page), int(size))})
    return dumps(res)
