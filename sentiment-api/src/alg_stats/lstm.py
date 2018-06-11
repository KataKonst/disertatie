import tflearn
from tflearn.data_utils import to_categorical, pad_sequences
import string
import numpy as nm
import codecs
import re
import collections
import math
import tensorflow as tf
import random
import glob
import pickle

allWords = []
trainDocuments = []
trainLabels = []
testDocuments = []
testLabels = []
lang = "en/"

def readFile(fileName, allWords):


    file = codecs.open(fileName, encoding='utf-8')
    for line in file:
        line = line.lower().encode('utf-8')
        words = line.split()
        for word in words:
            word = word.translate(None, string.punctuation.encode('utf-8'))
            if word != '':
                allWords.append(word)
    file.close()


def readFileToConvertWordsToIntegers(dictionary, fileName, allDocuments, allLabels, label):

    file = codecs.open(fileName, encoding='utf-8')
    document = []
    for line in file:
        line = line.lower().encode('utf-8')
        words = line.split()
        for word in words:
            word = word.translate(None, string.punctuation.encode('utf-8'))
            if word in dictionary:
                index = dictionary[word]
            else:
                index = 0
            document.append(index)
    file.close()
    if len(document)<150:
       allDocuments.append(document)
       allLabels.append(label)


vocabulary_size = 10000

def build_dataset(words):
  count = [['UNK', -1]]
  count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
  dictionary = dict()
  for word, _ in count:
    dictionary[word] = len(dictionary)
  data = list()
  for word in words:
    if word in dictionary:
      index = dictionary[word]
    else:
      index = 0
    data.append(index)
  return dictionary



fileList = glob.glob(lang+"/train/neg/*.txt")
for file in fileList:
    readFile(file, allWords)

fileList = glob.glob(lang+"/train/pos/*.txt")
for file in fileList:
    readFile(file, allWords)

fileList = glob.glob(lang+"/test/neg/*.txt")
for file in fileList:
    readFile(file, allWords)

fileList = glob.glob(lang+"/test/pos/*.txt")
for file in fileList:
    readFile(file, allWords)

dictionary = build_dataset(allWords)
del allWords

print("dict")
pickle.dump( dictionary, open( "dictionary.pickle", "wb" ) )
print("dict ready")
fileList = glob.glob(lang+"/train/neg/*.txt")
for file in fileList:
    readFileToConvertWordsToIntegers(dictionary, file, trainDocuments, trainLabels, 0)
print("neg: "+str(len(trainDocuments)))
fileList = glob.glob(lang+"/train/pos/*.txt")
for file in fileList:
    readFileToConvertWordsToIntegers(dictionary, file, trainDocuments, trainLabels, 1)
print("pos: "+str(len(trainDocuments)))
fileList = glob.glob(lang+"/test/neg/*.txt")
for file in fileList:
    readFileToConvertWordsToIntegers(dictionary, file, testDocuments, testLabels, 0)
print("test neg"+str(len(testDocuments)))
fileList = glob.glob(lang+"/test/pos/*.txt")
for file in fileList:
    readFileToConvertWordsToIntegers(dictionary, file, testDocuments, testLabels, 1)
print("test pos"+str(len(testDocuments)))

trainX = trainDocuments
testX = testDocuments
trainY = trainLabels
testY = testLabels

trainX = pad_sequences(trainX, maxlen=150, value=0.)
testX = pad_sequences(testX, maxlen=150, value=0.)
trainY = to_categorical(trainY, nb_classes=2)
testY = to_categorical(testY, nb_classes=2)
net = tflearn.input_data([None, 150])
net = tflearn.embedding(net, input_dim=vocabulary_size, output_dim=128)
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=0.001,
                         loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(trainX, trainY, validation_set=(testX, testY), show_metric=True,
          batch_size=32)
model.save("entf.tfl")

