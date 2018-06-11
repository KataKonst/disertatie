import tflearn
import pickle
import numpy as nm
import string
import tensorflow as tf


class TFAnalyzer:
    model = None
    dictionary = None

    def init(self):
        f = open('/home/katakonst/disertatie/sent-proj/sentiment-api/src/analysis/tfro/dictionary.pickle', 'rb')
        self.dictionary = pickle.load(f)
        f.close()
        tf.reset_default_graph()
        net = tflearn.input_data([None, 150])
        net = tflearn.embedding(net, input_dim=10000, output_dim=128)
        net = tflearn.lstm(net, 128, dropout=0.8)
        net = tflearn.fully_connected(net, 2, activation='softmax')
        net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
                                 loss='categorical_crossentropy')
        self.model = tflearn.DNN(net, tensorboard_verbose=0)
        self.model.load("/home/katakonst/disertatie/sent-proj/sentiment-api/src/analysis/tfro/rotf.tfl",  weights_only=True)


    def analyze(self, text):
        result = self.model.predict([self.convertTextToIndex(self.dictionary, text)])
        return {"negative": str(result[0][0]), "positive": str(result[0][1]) }

    def convertTextToIndex(self, dictionary, text):
        document = []
        text = text.lower().encode('utf-8')
        words = text.split()
        for word in words:
            word = word.translate(None, string.punctuation.encode('utf-8'))
            if word in dictionary:
                index = dictionary[word]
            else:
                index = 0
            document.append(index)
        ln = 150 - len(document)
        if ln>0 :
          document = nm.pad(document, (0, ln), 'constant')
        return document

