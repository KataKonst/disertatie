from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report,accuracy_score
import six.moves.cPickle as pickle

def main():
    lang="en"
    f = open(lang+'train.pkl', 'rb')
    reviews = pickle.load(f)
    f.close()
    f = open(lang+'test.pkl', 'rb')
    test = pickle.load(f)
    f.close()

    vectorizer = CountVectorizer()
    nb = MultinomialNB()

    train_features = vectorizer.fit_transform(reviews[0])
    test_features = vectorizer.transform(test[0])

    nb.fit(train_features, reviews[1])
    prediction_liblinear = nb.predict(test_features)
    print((classification_report(test[1], prediction_liblinear)))
    print(("accuracy: {0}".format( accuracy_score(test[1], prediction_liblinear))))


if __name__ == '__main__':
    main()
