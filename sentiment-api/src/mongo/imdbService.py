from pymongo import MongoClient
from analysis.services.vaderServiceEn import VaderServiceEn
from analysis.services.stanfordService import StanfordService
from analysis.services.naiveBayesService import NaiveBayesService
from analysis.services.svmService import SVMService
from analysis.services.tfService import TFService
from analysis.services.tfServiceRO import TFServiceRO
from analysis.services.meService import MaximumEntropyService

vaderService = VaderServiceEn()
stanfordService = StanfordService()
bayesService = NaiveBayesService("en")
svmService =SVMService("en")
tfService = TFService()
meService = MaximumEntropyService("en")
bayesServiceRO =NaiveBayesService("ro")
svmServiceRO = SVMService("ro")
tfServiceRO =  TFServiceRO()
meServiceRO = MaximumEntropyService("ro")


class ImdbService:
    client = MongoClient('localhost', 27017)
    reviews=[]

    def addWithSentiment(self, review, sentiment, type):
        try:
            vadeScore = vaderService.getScore(review["text"])
            review["vader"] = vadeScore
            review["svm"] = 1 if svmService.getScore(review["text"]) == "positive" else 0
            review["bayes"] = 1 if bayesService.getScore(review["text"]) == "positive" else 0
            review["me"] = 1 if meService.getScore(review["text"]) == "positive" else 0
            review["tf"] = tfService.getScore(review["text"])
            review["sentiment"]= sentiment
            review["type"]= type
            review["language"]= "en"
            db = self.client['imdb']
            collection = db['reviews']
            collection.insert_one(review)
          ##  game["stanford"] = {"result": stanfordService.getScore(game["review"])}

        except Exception as e:
          print(e)


    def addWithSentimentRO(self, review, sentiment, type):
        try:
            vadeScore = vaderService.getScore(review["text"])
            review["vader"] = vadeScore
            review["svm"] = 1 if svmServiceRO.getScore(review["text"]) == "positive" else 0
            review["bayes"] = 1 if bayesServiceRO.getScore(review["text"]) == "positive" else 0
            review["me"] = 1 if meServiceRO.getScore(review["text"]) == "positive" else 0
            review["tf"] = tfServiceRO.getScore(review["text"])
            review["sentiment"]= sentiment
            review["type"]= type
            review["language"]= "ro"
            db = self.client['imdb']
            collection = db['reviews']
            collection.insert_one(review)
          ##  game["stanford"] = {"result": stanfordService.getScore(game["review"])}

        except Exception as e:
          print(e)

    def findByType(self, type, language, page, size):
        db = self.client['imdb']
        collection = db["reviews"]
        if type != "all":
          return collection.find({'type': type, 'language': language}) \
            .skip(page * size - size).limit(size)

        return collection.find({'language': language}) \
            .skip(page * size - size).limit(size)

    def countReviews(self, type, language):
        db = self.client['imdb']
        collection = db["reviews"]
        if type != "all":
            return collection.find({'type': type, 'language': language}).count()

        return collection.find({'language': language}).count()
