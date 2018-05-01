from pymongo import MongoClient
from analysis.services.vaderServiceEn import VaderServiceEn
from analysis.services.stanfordService import StanfordService
from analysis.services.naiveBayesService import NaiveBayesService
from analysis.services.svmService import SVMService
from mongo.tweetService import TweetService

vaderService = VaderServiceEn()
tweetService = TweetService()
stanfordService = StanfordService()
bayesService = NaiveBayesService()
svmService = SVMService()

class GameService:
    client = MongoClient('localhost', 27017)

    def countGames(self):
        db = self.client['games']
        collection =  db['games']
        return  collection.find().count()

    def add(self, game):
        db = self.client['games']
        collection = db['games']
        collection.insert_one(game)

    def addWithSentiment(self, game, name):
        vadeScore = vaderService.getScore(game["review"])
        game["vader"] = vadeScore
        game["game"] = name
        game["svm"] = 1 if svmService.getScore(game["review"]) == "positive" else 0
        game["bayes"] = 1 if bayesService.getScore(game["review"]) == "positive" else 0
      ##  game["stanford"] = {"result": stanfordService.getScore(game["review"])}
        db = self.client['games']
        collection = db['reviews']
        collection.insert_one(game)

    def all(self):
        db = self.client['games']
        collection = db['games']
        return collection.find({})

    def findByName(self, name,page,size):
         db = self.client['games']
         collection = db["reviews"]
         return collection.find({'game': name}).skip(page*size-size).limit(size)

    def countReviewsByGame(self,name):
        db = self.client['games']
        collection = db["reviews"]
        return collection.find({'game': name}).count()

    def processForGame(self, name):
        db = self.client['games']
        collection = db[name]
        res=collection.find()
        vaderService = VaderServiceEn()
        for review in res:
             review["vader"] = vaderService.getScore(review["review"])
             collection.save(review)

    def averrageByStanford(self,page, size):
        db = self.client['games']
        collection = db['reviews']
        skipSize = page * size -size
        return list(collection.aggregate([{'$group':{
           '_id': "$game",
           'avg': { '$avg': "$stanford.result" },
           'count': { '$sum': 1 }
            }
          },
            {'$sort': { 'avg': -1}},
            {'$facet': {
                'metadata': [{ '$count': "total"}, { '$addFields': {'page': 'NumberInt(3)'}}],
        'data': [{ '$skip': skipSize}, { '$limit': size}]
        }}
              ]))

    def averrageBySvm(self,page, size):
        db = self.client['games']
        collection = db['reviews']
        skipSize = page * size -size
        return list(collection.aggregate([{'$group':{
         '_id': "$game",
           'avg': { '$avg': "$svm" },
           'count': { '$sum': 1 }
            }
          },
            {'$sort': { 'avg': -1}},
            {'$facet': {
                'metadata': [{ '$count': "total"}, { '$addFields': {'page': 'NumberInt(3)'}}],
        'data': [{ '$skip': skipSize}, { '$limit': size}]
        }}
              ]))

    def averrageByBayes(self, page, size):
        db = self.client['games']
        collection = db['reviews']
        skipSize = page * size - size
        return list(collection.aggregate([{'$group': {
            '_id': "$game",
            'avg': {'$avg': "$bayes"},
            'count': {'$sum': 1}
        }
        },
            {'$sort': {'avg': -1}},
            {'$facet': {
                'metadata': [{'$count': "total"}, {'$addFields': {'page': 'NumberInt(3)'}}],
                'data': [{'$skip': skipSize}, {'$limit': size}]
            }}
        ]))

    def averrageByVader(self, page, size):
        db = self.client['games']
        collection = db['reviews']
        skipSize = page * size - size
        return list(collection.aggregate([{'$group': {
            '_id': "$game",
            'avg': {'$avg': "$vader.compound"},
            'count': {'$sum': 1}
        }
        },
            {'$sort': {'avg': -1}},
            {'$facet': {
                'metadata': [{'$count': "total"}, {'$addFields': {'page': 'NumberInt(3)'}}],
                'data': [{'$skip': skipSize}, {'$limit': size}]
            }}
        ]))
