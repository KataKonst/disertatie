import jsonlines
from gameService import GameService

games=GameService()
with jsonlines.open('/home/katakonst/disertatie/datasets/steam_reviews/data/Warframe.jsonlines') as reader:
    for obj in reader:
        games.add(obj, 'Warframe')
