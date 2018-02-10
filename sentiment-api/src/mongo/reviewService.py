from pymongo import MongoClient

class ReviewService:
    client = MongoClient('localhost', 27017)

    def findByGame(self, name,page,size):
        db = self.client['games']
        collection = db['games']
        game = collection.find_one({'name': name})
        print(game)
        collection = db[game.get('colectionName')]
        return  collection.find({}).skip(page*size-size).limit(size)

    def countByGame(self, name):
        db = self.client['games']
        collection = db['games']
        game = collection.find_one({'name': name})
        print(game)
        collection = db[game.get('colectionName')]
        return collection.find({}).count()
