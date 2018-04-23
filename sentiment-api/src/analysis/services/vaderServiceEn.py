from nltk.sentiment.vader import SentimentIntensityAnalyzer
from unidecode import unidecode

class VaderServiceEn:
    analyzer = SentimentIntensityAnalyzer()
    def getScore(self, review):
        return self.analyzer.polarity_scores(unidecode(review.lower()))


