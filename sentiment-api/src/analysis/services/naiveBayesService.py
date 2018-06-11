from analysis.bayes.naive import NaiveBayes
from unidecode import unidecode

class NaiveBayesService:

    analyzer = None
    def __init__(self, language):
      self.analyzer = NaiveBayes()
      self.analyzer.init(language)

    def getScore(self, review):
        return self.analyzer.analyze(unidecode(review.lower()))


