from analysis.tf.tf import TFAnalyzer
from unidecode import unidecode

class TFService:
    analyzer = TFAnalyzer()
    analyzer.init()

    def getScore(self, review):
        return self.analyzer.analyze(unidecode(review.lower()))


