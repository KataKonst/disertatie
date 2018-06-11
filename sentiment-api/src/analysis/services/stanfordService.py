from pycorenlp import StanfordCoreNLP

class StanfordService:
        nlp = StanfordCoreNLP('http://localhost:9000')

        def getScore(self, review):
            res = self.nlp.annotate(review,
                         properties={
                             'annotators': 'sentiment',
                             'outputFormat': 'json',
                             'timeout': 1000,
                         })

            if type(res) is str:
                return 0

            sentiment=0
            for sent in res["sentences"] :
                  sentiment += int(sent["sentimentValue"])

            return sentiment/len(res["sentences"])






