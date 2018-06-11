from flask import Blueprint
from mongo.imdbService import ImdbService
from bson.json_util import dumps

imdb = Blueprint('imdb', __name__, template_folder='web')
imdbService = ImdbService()

@imdb.route('/type/<type>/language/<language>/page/<page>/size/<size>')
def getIMDBReviews(type, language, page, size):
    res = dict({'length': imdbService.countReviews(type, language),
                'results': imdbService.findByType(type, language, int(page), int(size))})
    return dumps(res)