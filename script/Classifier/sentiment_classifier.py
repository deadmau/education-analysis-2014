#import pickle, feature, nltk.classify
import pickle, feature
from nltk.classify import *
from feature import *

if __name__ == '__main__':

    try:
        f = open('../../data/raw/classifier.pkl', 'rb')
        NBClassifier = pickle.load(f)
        f.close()
    except (OSError, IOError):
        print "File 'classifier.pkl' not found"
        exit(1)

    # Test the classifier
    testTweet = 'The only thing more disappointing  than the undertaker losing is the US education system'
    testTweet2 = "can we skip this whole college thing and go straight and go to the part where i have an awesome job and spend all my time traveling?"
    testTweet3 = 'Really going to be a struggle to go to college today'
    stopWords = getStopWordList('../../data/raw/stopwords.txt')
    processedTestTweet = processTweet(testTweet)
    processedTestTweet2 = processTweet(testTweet2)
    processedTestTweet3 = processTweet(testTweet3)
    print NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords)))
    print NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet2, stopWords)))
    print NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet3, stopWords)))
