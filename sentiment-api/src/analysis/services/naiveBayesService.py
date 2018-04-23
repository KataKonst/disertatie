from analysis.bayes.naive import NaiveBayes
from unidecode import unidecode

class NaiveBayesService:
    analyzer = NaiveBayes()
    analyzer.init()

    def getScore(self, review):
        return self.analyzer.analyze(unidecode(review.lower()))


