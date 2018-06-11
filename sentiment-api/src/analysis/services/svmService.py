from analysis.svm.svm import SVM
from unidecode import unidecode

class SVMService:
    analyzer = None
    def __init__(self, language):
     self.analyzer = SVM()
     self.analyzer.init(language)

    def getScore(self, review):
        return self.analyzer.analyze(unidecode(review.lower()))


