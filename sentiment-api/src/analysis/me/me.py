import pickle
from io import open
from nltk.corpus import stopwords
from nltk.classify import MaxentClassifier
import re

class MaximumEntropy:

  classifier = None

  def word_feats(self, words):
    return dict([(word, True) for word in words])

  def processWords(self, inputText):
    result = []
    trash_characters = '?.,!:;"$%^&*()#@+/0123456789<>=\\[]_~{}|`'
    trans = str.maketrans(trash_characters, ' ' * len(trash_characters))
    text = re.sub(r'[^\x00-\x7F]+', ' ', inputText)
    text = text.translate(trans)
    text = ' '.join([w for w in text.split()])
    words = []
    for word in text.split():
        words.append(word.lower())
        text = ' '.join(words)
        result.append(text.strip())
    return result

  def init(self, language):
      path = "/home/katakonst/disertatie/sent-proj/sentiment-api/src/analysis/me/"
      f = open(path + 'train.pkl', 'rb') if language == "en" else open(path + 'rotrain.pkl', 'rb')
      reviews = pickle.load(f)
      f.close()
      negfeats = []
      posfeats = []
      for i,rev in enumerate(reviews[0]):
          if reviews[1][i] == 0:
              negfeats.append((self.word_feats(rev.split()), "0"))
          else:
              posfeats.append((self.word_feats(rev.split()), "1"))

      trainfeats = negfeats + posfeats
      self.classifier = MaxentClassifier.train(trainfeats, 'GIS', trace=0, encoding=None, labels=None, gaussian_prior_sigma=0,
                                    max_iter=1)

  def analyze(self, text):
      prediction = self.classifier.classify(self.word_feats(self.processWords(text)))
      if prediction == "1":
          return "positive"

      return "negative"
