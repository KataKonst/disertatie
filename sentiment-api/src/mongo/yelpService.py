from pymongo import MongoClient
from analysis.services.vaderServiceEn import VaderServiceEn
from analysis.services.stanfordService import StanfordService
from analysis.services.naiveBayesService import NaiveBayesService
from analysis.services.svmService import SVMService

vaderService = VaderServiceEn()
stanfordService = StanfordService()
bayesService = NaiveBayesService()
svmService = SVMService()

class YelpService:
    client = MongoClient('localhost', 27017)

    def countGames(self):
        db = self.client['yelp']
        collection =  db['reviews']
        return  collection.find().count()

    def add(self, game):
        db = self.client['yelp']
        collection = db['reviews']
        collection.insert_one(game)

    def addBusiness(self, business):
        db = self.client['yelp']
        collection = db['business']
        collection.insert_one(business)

    def findBusiness(self, id):
        db = self.client['yelp']
        collection =  db['business']
        return collection.find_one({'business_id': id})


    def addWithSentiment(self, review):
        try:
            vadeScore = vaderService.getScore(review["text"])
            review["vader"] = vadeScore
            business = self.findBusiness(review["business_id"])
            review["business_name"]= business["name"]
            review["svm"] = 1 if svmService.getScore(review["text"]) == "positive" else 0
            review["bayes"] = 1 if bayesService.getScore(review["text"]) == "positive" else 0
          ##  game["stanford"] = {"result": stanfordService.getScore(game["review"])}
            db = self.client['yelp']
            collection = db['reviews']
            collection.insert_one(review)
        except ValueError:
          print("error")

    def all(self):
        db = self.client['games']
        collection = db['games']
        return collection.find({})

    def findByName(self, name,page,size):
         db = self.client['yelp']
         collection = db["reviews"]
         return collection.find({'business_name':  {"$regex": name}})\
             .skip(page*size-size).limit(size)

    def countReviewsByName(self,name):
        db = self.client['yelp']
        collection = db["reviews"]
        return collection.find({'business_name': {"$regex": name}}).count()

    def processForGame(self, name):
        db = self.client['games']
        collection = db[name]
        res=collection.find()
        vaderService = VaderServiceEn()
        for review in res:
             review["vader"] = vaderService.getScore(review["review"])
             collection.save(review)

    def averrageByStanford(self,page, size):
        db = self.client['yelp']
        collection = db['reviews']
        skipSize = page * size -size
        return list(collection.aggregate([{'$group':{
           '_id': "$business_name",
           'avg': { '$avg': "$stanford.result" },
           'count': { '$sum': 1 }
            }
          },
            {'$sort': { 'avg': -1}},
            {'$facet': {
                'metadata': [{ '$count': "total"},
                             { '$addFields': {'page': 'NumberInt(3)'}}],
        'data': [{ '$skip': skipSize}, { '$limit': size}]
        }}
              ]))

    def averrageBySvm(self,page, size):
        db = self.client['yelp']
        collection = db['reviews']
        skipSize = page * size -size
        return list(collection.aggregate([{'$group':{
         '_id': "$business_name",
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
        db = self.client['yelp']
        collection = db['reviews']
        skipSize = page * size - size
        return list(collection.aggregate([{'$group': {
            '_id': "$business_name",
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
        db = self.client['yelp']
        collection = db['reviews']
        skipSize = page * size - size
        return list(collection.aggregate([{'$group': {
            '_id': "$business_name",
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
