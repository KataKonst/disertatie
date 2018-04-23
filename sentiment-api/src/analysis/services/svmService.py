from analysis.svm.svm import SVM
from unidecode import unidecode

class SVMService:
    analyzer = SVM()
    analyzer.init()

    def getScore(self, review):
        return self.analyzer.analyze(unidecode(review.lower()))


