from pymongo import MongoClient
from analysis.services.vaderServiceEn import VaderServiceEn

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

    def all(self,page,size):
        db = self.client['games']
        collection = db['games']
        return collection.find({}).skip(page*size-size).limit(size)

    def findByName(self, name,page,size):
         db = self.client['games']
         collection = db[name]
         return collection.find().skip(page*size-size).limit(size)

    def countReviewsByGame(self,name):
        db = self.client['games']
        collection = db[name]
        return collection.find().count()

    def processForGame(self, name):
        db = self.client['games']
        collection = db[name]
        res=collection.find()
        vaderService = VaderServiceEn()
        for review in res:
             review["vader"] = vaderService.getScore(review["review"])
             collection.save(review)
