from nltk.sentiment.vader import SentimentIntensityAnalyzer

class VaderServiceEn:
    analyzer = SentimentIntensityAnalyzer()

    def getScore(self, review):
        return self.analyzer.polarity_scores(review)


