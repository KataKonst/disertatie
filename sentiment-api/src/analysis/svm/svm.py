from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from nltk.corpus import stopwords
import re


class SVM:
    vectorizer = TfidfVectorizer(min_df=5, max_df=0.8,
                                 sublinear_tf=True, use_idf=True)
    clasifier = svm.LinearSVC()

    def init(self):
        f = open('/home/katakonst/disertatie/sent-proj/sentiment-api/src/analysis/svm/train.pkl', 'rb')
        reviews = pickle.load(f)
        f.close()
        train_features = self.vectorizer.fit_transform(reviews[0])
        self.clasifier.fit(train_features, reviews[1])


    def analyze(self, text):
        input_features = self.vectorizer.transform(self.processWords(text))
        print(input_features)
        prediction = self.clasifier.predict(input_features)
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
