from pycorenlp import StanfordCoreNLP
from operator import attrgetter

class StanfordService:
        nlp = StanfordCoreNLP('http://localhost:9000')

        def getScore(self, review):
            res = self.nlp.annotate(review,
                         properties={
                             'annotators': 'sentiment',
                             'outputFormat': 'json',
                             'timeout': 1000,
                         })

            sentiment = 0
            for sent in res["sentences"] :
                  print(sent["sentimentValue"]+ " "+" ".join([t["word"] for t in sent["tokens"]]))
                  sentiment += int(sent["sentimentValue"])

            return sentiment/len(res["sentences"])






