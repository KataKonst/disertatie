from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from io import open
import pickle
from nltk.corpus import stopwords
import re

class NaiveBayes:
    vectorizer = CountVectorizer()
    nb = MultinomialNB()

    def init(self):
            f = open('/home/katakonst/disertatie/sent-proj/sentiment-api/src/analysis/bayes/train.pkl', 'rb')
            reviews = pickle.load(f)
            f.close()
            train_features = self.vectorizer.fit_transform([r for r in reviews[0]])
            self.nb.fit(train_features, [int(r) for r in reviews[1]])

    def analyze(self, text):
        input_features = self.vectorizer.transform(self.processWords(text))
        prediction = self.nb.predict(input_features)
        if prediction[0] == 1:
            return "positive"
        else:
            return "negative"

    def processWords(self, inputText):
        result = []
        stop = stopwords.words('english')
        trash_characters = '?.,!:;"$%^&*()#@+/0123456789<>=\\[]_~{}|`'
        trans = str.maketrans(trash_characters, ' ' * len(trash_characters))
        text = re.sub(r'[^\x00-\x7F]+', ' ', inputText)
        text = text.translate(trans)
        text = ' '.join([w for w in text.split() if w not in stop])
        words = []
        for word in text.split():
            if len(word) > 2:
                words.append(word.lower())
            text = ' '.join(words)
            result.append(text.strip())
        return result
