import jsonlines
from mongo.gameService import GameService
import os

games=GameService()
for filename in os.listdir("/home/katakonst/disertatie/Yelp/yelp_challenge/yelp_phoenix_academic_dataset/yelp_academic_dataset_business.json"):
     with jsonlines.open("/home/katakonst/disertatie/steam_reviews/data/"+filename) as reader:
       for obj in reader:
        file=filename.replace('.jsonlines', "")
        file = file.replace("_"," ");
        games.addWithSentiment(obj, file)
