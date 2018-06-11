from analysis.me.me import MaximumEntropy
from unidecode import unidecode

class MaximumEntropyService:

    analyzer = None
    def __init__(self, language):
      self.analyzer = MaximumEntropy()
      self.analyzer.init(language)

    def getScore(self, review):
        return self.analyzer.analyze(unidecode(review.lower()))


