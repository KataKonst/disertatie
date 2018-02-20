from pymongo import MongoClient


class TweetService:
    client = MongoClient('localhost', 27017)

    def add(self, tweet):
        db = self.client['tweets']
        collection = db['tweet']
        collection.insert_one(tweet)

    def findByLocation(self, location, page, size):
        db = self.client['tweets']
        collection = db['tweet']
        return collection.find({'place.name': location},
                               {"text": "1", "vader": "1"}).skip(page * size - size).limit(size)

    def countByLocation(self, location):
        db = self.client['tweets']
        collection = db['tweet']
        return collection.find({'place.name': location}).count();

    def averrageByLocation(self,page, size):
        db = self.client['tweets']
        collection = db['tweet']
        skipSize = page * size -size
        return collection.aggregate([{'$group':{
                                                '_id': {'place': "$place.full_name"},
           'avg': { '$avg': "$vader.compound" },
           'count': { '$sum': 1 }
            }
          },
            { '$skip':  skipSize },
            {'$sort': { 'avg': -1}}
              ])

    def averrageByLocationCount(self):
            db = self.client['tweets']
            collection = db['tweet']
            return collection.aggregate([{"$group": {"_id": "place.full_name", "count": {"$sum":1} }}])



