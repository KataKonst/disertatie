from flask import Blueprint, request
from analysis.services.vaderService import VaderService
from analysis.services.vaderServiceEn import VaderServiceEn
from analysis.services.stanfordService import StanfordService
from flask import jsonify
from mongo.reviewService import ReviewService
from bson.json_util import dumps


vaderService = VaderService()
vaderServiceEn = VaderServiceEn()
stanfordService = StanfordService()
reviewService = ReviewService()
reviews = Blueprint('product', __name__, template_folder='web')

@reviews.route('/language/<language>/method/<method>', methods=['POST'])
def analizeReview(language, method):
    content = request.json

    if language == 'ro' and method == 'vader':
        score =dict(results = vaderService.getScore(content['input']),method = "vader")
        return jsonify(score)

    if language == 'en' and method == 'vader':
        score =dict(results = vaderServiceEn.getScore(content['input']),method = "vader")
        return jsonify(score)

    if language == 'en' and method == 'stanford':
        score =dict(results = stanfordService.getScore(content['input']),method = "stanford")
        return jsonify(score)

    return "not implemented"


@reviews.route('/col/<name>/page/<page>/size/<size>')
def searchByCollection(name, page, size):
      res = dict({'length': reviewService.countByGame(name),
                    'results': reviewService.findByGame(name, int(page), int(size))})
      return dumps(res)
