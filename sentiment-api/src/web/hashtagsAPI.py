from flask import Blueprint
from mongo.tweetService import TweetService
from bson.json_util import dumps

hashtags = Blueprint('hashtag', __name__, template_folder='web')
tweetService = TweetService()


@hashtags.route('/average/page/<page>/size/<size>/alg/<algorithm>')
def averrage(page, size, algorithm):

    if algorithm == 'vader':
        results = tweetService.averrageByHashTagsVader(int(page), int(size))
        return dumps(dict({'length': results[0]['metadata'][0]['total'],
                           'results': results[0]['data']}))

    if algorithm == 'stanford':
        results = tweetService.averrageByHashTagsStanford(int(page), int(size))
        return dumps(dict({'length':results[0]['metadata'][0]['total'],
                'results': results[0]['data']}))

    return ""

@hashtags.route('/hashtag/<hashtag>/page/<page>/size/<size>')
def searchByHashtag(hashtag, page, size):
    res = dict({'length' :tweetService.countByHashTag(hashtag),
                'results': tweetService.findByHashtag(hashtag, int(page), int(size))})
    return dumps(res)