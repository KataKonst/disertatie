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


    def findByLocationFullName(self, location, page, size):
        db = self.client['tweets']
        collection = db['tweet']
        return collection.find({'place.full_name': location},
                               {"text": "1", "vader": "1"}).skip(page * size - size).limit(size)

    def countByLocation(self, location):
        db = self.client['tweets']
        collection = db['tweet']
        return collection.find({'place.name': location}).count()

    def countByLocationFullName(self, location):
        db = self.client['tweets']
        collection = db['tweet']
        return collection.find({'place.full_name': location}).count()

    def averrageByLocation(self,page, size):
        db = self.client['tweets']
        collection = db['tweet']
        skipSize = page * size -size
        return list(collection.aggregate([{'$group':{
                                                '_id': "$place.full_name",
           'avg': { '$avg': "$vader.compound" },
           'count': { '$sum': 1 }
            }
          },
            {'$sort': { 'avg': -1}},
            {'$facet': {
                'metadata': [{ '$count': "total"}, { '$addFields': {'page': 'NumberInt(3)'}}],
        'data': [{ '$skip': skipSize}, { '$limit': size}]
        }}
              ]))

    def averrageByLocationStanford(self,page, size):
        db = self.client['tweets']
        collection = db['tweet']
        skipSize = page * size -size
        return list(collection.aggregate([{'$group':{
                                                '_id': "$place.full_name",
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

    def averrageByHashTagsVader(self,page, size):
        db = self.client['tweets']
        collection = db['tweet']
        skipSize = page * size -size
        return list(collection.aggregate([
            { '$unwind': "$entities.hashtags"},
            {'$group':{
              '_id': "$entities.hashtags.text",
           'avg': { '$avg': "$vader.compound" },
           'count': { '$sum': 1 }
            }
          },
            {'$sort': { 'avg': -1}},
            {'$facet': {
                'metadata': [{ '$count': "total"}, { '$addFields': {'page': 'NumberInt(3)'}}],
        'data': [{ '$skip': skipSize}, { '$limit': size}]
        }}
              ]))

    def averrageByHashTagsStanford(self, page, size):
        db = self.client['tweets']
        collection = db['tweet']
        skipSize = page * size - size
        return list(collection.aggregate([
            { '$unwind': "$entities.hashtags"},
        {'$group': {
            '_id': "$entities.hashtags.text",
            'avg': {'$avg': "$stanford.result"},
            'count': {'$sum': 1}
        }
        },
            {'$sort': {'avg': -1}},
            {'$facet': {
                'metadata': [{'$count': "total"}, {'$addFields': {'page': 'NumberInt(3)'}}],
                'data': [{'$skip': skipSize}, {'$limit': size}]
            }}
        ]))

    def findByHashtag(self, hashtag, page, size):
        db = self.client['tweets']
        collection = db['tweet']
        return collection.find({
       'entities.hashtags.text': { '$in': [ hashtag ] } } ).skip(page * size - size).limit(size)

    def countByHashTag(self, hashtag):
        db = self.client['tweets']
        collection = db['tweet']
        return  collection.find({
       'entities.hashtags.text': { '$in': [ hashtag ] } }) .count()




