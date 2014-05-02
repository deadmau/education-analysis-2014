#import pickle, feature, nltk.classify
import pickle, feature
from nltk.classify import *
from feature import *

if __name__ == '__main__':

    try:
        f = open('dataset/classifier.pkl', 'rb')
        NBClassifier = pickle.load(f)
        f.close()
    except (OSError, IOError):
        print "File 'classifier.pkl' not found"
        exit(1)

    # Test the classifier
    testTweet = 'The only thing more disappointing  than the undertaker losing is the US education system'
    stopWords = getStopWordList('dataset/stopwords.txt')
    processedTestTweet = processTweet(testTweet)
    print NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
