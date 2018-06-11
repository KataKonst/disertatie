from analysis.tfro.tf import TFAnalyzer
from unidecode import unidecode

class TFServiceRO:

    analyzer = TFAnalyzer()
    analyzer.init()

    def getScore(self, review):
        return self.analyzer.analyze(unidecode(review.lower()))


