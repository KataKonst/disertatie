import pickle
from io import open
import collections
import nltk.metrics
from nltk.classify import MaxentClassifier
from nltk.metrics import precision, recall, f_measure
from nltk.corpus import stopwords
import re

f = open('rotrain.pkl', 'rb')
reviews = pickle.load(f)
f.close()

f = open('rotest.pkl', 'rb')
test = pickle.load(f)
f.close()


def word_feats(words):
    return dict([(word, True) for word in words])


def processWords(inputText):
    result = []
    trash_characters = '?.,!:;"$%^&*()#@+/0123456789<>=\\[]_~{}|`'
    trans = str.maketrans(trash_characters, ' ' * len(trash_characters))
    text = re.sub(r'[^\x00-\x7F]+', ' ', inputText)
    text = text.translate(trans)
    text = ' '.join([w for w in text.split()])
    words = []
    for word in text.split():
        if len(word) > 2:
            words.append(word.lower())
        text = ' '.join(words)
        result.append(text.strip())
    return result

def main():
    negfeats = []
    posfeats = []
    for i, f in enumerate(reviews[0]):
        print(f)
        if reviews[1][i] == 0:
            negfeats.append((word_feats(f.split()), "neg"))
        else:
            posfeats.append((word_feats(f.split()), "pos"))

    testNegfeats = []
    testPosfeats = []
    for i,f in enumerate(test[0]) :
        if test[1][i] == 0:
            testNegfeats.append((word_feats(f.split()), "neg"))
        else:
            testPosfeats.append((word_feats(f.split()), "pos"))


    trainfeats = negfeats + posfeats
    testfeats = testNegfeats + testPosfeats


    print('train on %d instances, test on %d instances - Maximum Entropy' % (len(trainfeats), len(testfeats)))

    classifier = MaxentClassifier.train(trainfeats, 'GIS', trace=0, encoding=None, labels=None, gaussian_prior_sigma=0,
                                        max_iter=1)

    refsets = collections.defaultdict(set)
    testsets = collections.defaultdict(set)
    for i, (feats, label) in enumerate(testfeats):
        refsets[label].add(i)
        observed = classifier.classify(feats)
        testsets[observed].add(i)

    accuracy = nltk.classify.util.accuracy(classifier, testfeats)
    pos_precision = precision(refsets['pos'], testsets['pos'])
    pos_recall = recall(refsets['pos'], testsets['pos'])
    pos_fmeasure = f_measure(refsets['pos'], testsets['pos'])
    neg_precision = precision(refsets['neg'], testsets['neg'])
    neg_recall = recall(refsets['neg'], testsets['neg'])
    neg_fmeasure = f_measure(refsets['neg'], testsets['neg'])
    print(pos_recall)
    print(neg_recall)
    print()
    print('')
    print('---------------------------------------')
    print('          Maximum Entropy              ')
    print('---------------------------------------')
    print('accuracy:', accuracy)
    print('precision', (pos_precision + neg_precision) / 2)
    print('recall', (pos_recall + neg_recall) / 2)
    print('f-measure', (pos_fmeasure + neg_fmeasure) / 2)


if __name__ == '__main__':
    main()