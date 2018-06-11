import jsonlines
from mongo.yelpService import YelpService

yelp=YelpService()
with jsonlines.open("/home/katakonst/disertatie/Yelp/yelp_challenge/yelp_phoenix_academic_dataset/yelp_academic_dataset_review.json") as reader:
    for obj in reader:
            yelp.addWithSentiment(obj)
