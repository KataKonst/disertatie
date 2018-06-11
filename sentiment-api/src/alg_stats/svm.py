from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
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

    vectorizer = TfidfVectorizer(min_df=5, max_df=0.8,
                                sublinear_tf=True, use_idf=True)
    train_features = vectorizer.fit_transform(reviews[0])
    test_features = vectorizer.transform(test[0])
    classifier_liblinear = svm.LinearSVC()
    classifier_liblinear.fit(train_features, reviews[1])
    prediction_liblinear = classifier_liblinear.predict(test_features)
    print((classification_report(test[1], prediction_liblinear)))
    print(("accuracy: {0}".format( accuracy_score(test[1], prediction_liblinear))))


if __name__ == '__main__':
    main()
