from flask import Blueprint, request
from analysis.services.vaderService import VaderService
from analysis.services.vaderServiceEn import VaderServiceEn
from analysis.services.stanfordService import StanfordService
from analysis.services.naiveBayesService import NaiveBayesService
from analysis.services.svmService import SVMService
from analysis.services.meService import MaximumEntropyService
from analysis.services.tfService import TFService
from analysis.services.tfServiceRO import TFServiceRO
from flask import jsonify
from mongo.reviewService import ReviewService
from bson.json_util import dumps


vaderService = VaderService()
vaderServiceEn = VaderServiceEn()
stanfordService = StanfordService()
reviewService = ReviewService()
bayesService = NaiveBayesService("en")
bayesServiceRO = NaiveBayesService("ro")
tfService = TFService()
tfServiceRO = TFServiceRO()
meService = MaximumEntropyService("en")
meServiceRO = MaximumEntropyService("ro")
svmService = SVMService("en")
svmServiceRO = SVMService("ro")


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

    if language == 'en' and method == 'bayes':
        score = dict(results=bayesService.getScore(content['input']), method="bayes")
        return jsonify(score)

    if language == 'ro' and method == 'bayes':
        score = dict(results=bayesServiceRO.getScore(content['input']), method="bayes")
        return jsonify(score)

    if language == 'en' and method == 'svm':
        score = dict(results=svmService.getScore(content['input']), method="svm")
        return jsonify(score)

    if language == 'ro' and method == 'svm':
        score = dict(results=svmServiceRO.getScore(content['input']), method="svm")
        return jsonify(score)

    if language == 'en' and method == 'tf':
        score = dict(results=tfService.getScore(content['input']), method="tf")
        return jsonify(score)

    if language == 'ro' and method == 'tf':
        score = dict(results=tfServiceRO.getScore(content['input']), method="tf")
        return jsonify(score)

    if language == 'en' and method == 'me':
        score = dict(results=meService.getScore(content['input']), method="me")
        return jsonify(score)

    if language == 'ro' and method == 'me':
        score = dict(results=meServiceRO.getScore(content['input']), method="me")
        return jsonify(score)

    return "not implemented"

@reviews.route('/col/<name>/page/<page>/size/<size>')
def searchByCollection(name, page, size):
      res = dict({'length': reviewService.countByGame(name),
                    'results': reviewService.findByGame(name, int(page), int(size))})
      return dumps(res)

