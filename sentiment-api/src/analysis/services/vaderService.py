from analysis.vader.vaderSentAnalisys import SentimentIntensityAnalyzer

class VaderService:
    analyzer = SentimentIntensityAnalyzer()
    def getScore(self, review):
        return self.analyzer.polarity_scores(review)





