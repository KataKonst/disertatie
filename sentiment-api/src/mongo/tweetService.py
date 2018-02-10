from pymongo import MongoClient

class TweetService:
    client = MongoClient('localhost', 27017)

    def add(self, tweet):
        db = self.client['tweets']
        collection = db['tweet']
        collection.insert_one(tweet)