from flask import Blueprint, request
from flask import json
from analysis.services.vaderService import VaderService
from analysis.services.vaderServiceEn import VaderServiceEn
from flask import jsonify
from mongo.reviewService import ReviewService
from bson.json_util import dumps


vaderService = VaderService()
vaderServiceEn = VaderServiceEn()
reviewService = ReviewService()
reviews = Blueprint('product', __name__, template_folder='web')

@reviews.route('/language/<language>/method/<method>', methods=['POST'])
def analizeReview(language, method):
    content = request.json

    if language == 'ro' and method == 'vader':
        return jsonify(vaderService.getScore(content['input']))

    if language == 'en' and method == 'vader':
        return jsonify(vaderServiceEn.getScore(content['input']))

    return "not implemented"


@reviews.route('/col/<name>/page/<page>/size/<size>')
def searchByCollection(name, page, size):
      res = dict({'length': reviewService.countByGame(name),
                    'results': reviewService.findByGame(name, int(page), int(size))})
      return dumps(res)
