from analysis.vader.vaderSentAnalisys import SentimentIntensityAnalyzer
from unidecode import unidecode

class VaderService:
    analyzer = SentimentIntensityAnalyzer()
    def getScore(self, review):
        return  self.analyzer.polarity_scores(unidecode(review.lower()))





