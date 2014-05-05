#import pickle, feature, nltk.classify
import pickle, feature, pandas as pd
from nltk.classify import *
from feature import *

#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    f = open('../../data/simulated/featureList.pkl', 'rb')
    featureList = pickle.load(f)
    f.close()
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end 

#classifies each tweet and store them in Pandas DataFrame
def classify_tweets(file_name):
    try:
        f = open('../../data/cleaned/'+file_name+'tweets.pkl', 'rb')
        tweets = pickle.load(f)
        f.close()
    except (OSError, IOError):
        print "File "+file_name+" not found"
        exit(1)
    stopWords = getStopWordList('../../data/raw/stopwords.txt')

    if isinstance(tweets, set): 
        data = {'text': [], 'sentiment':[]}
        for t in tweets:
            data['text'].append(t)
            data['sentiment'].append(NBClassifier.classify(extract_features(getFeatureVector(processTweet(t), stopWords))))
        finished = pd.DataFrame(data, columns=['text', 'sentiment'])
        f = open('../../data/simulated/'+file_name+'Analyzed.pkl', 'wb')
        pickle.dump(finished, f)
        f.close()

#classifies each keyword tweet and store them in Pandas DataFrame
def classify_keywords(filename):
    try:
        f = open('../../data/cleaned/'+filename+'OtherWordTweets.pkl', 'rb')
        tweets = pickle.load(f)
        f.close()
    except (OSError, IOError):
        print "File "+filename+" not found"
        exit(1)
    stopWords = getStopWordList('../../data/raw/stopwords.txt')

    if isinstance(tweets, dict): 
        data = {'keyword': [], 'text':[], 'sentiment':[]}
        for key in tweets.keys():
            for t in tweets[key]:
                data['keyword'].append(key)
                data['text'].append(t)
                data['sentiment'].append( NBClassifier.classify(extract_features(getFeatureVector(processTweet(t), stopWords))) )
        finished = pd.DataFrame(data, columns=['keyword', 'text', 'sentiment'])
        f = open('../../data/simulated/'+filename+'WordAnalyzed.pkl', 'wb')
        pickle.dump(finished, f)
        f.close()


if __name__ == '__main__':
    try:
        f = open('../../data/simulated/classifier.pkl', 'rb')
        NBClassifier = pickle.load(f)
        f.close()
    except (OSError, IOError):
        print "File 'classifier.pkl' not found"
        exit(1)
    #process tweets with location
    """
    classify_tweets('africa')
    classify_tweets('asia')
    classify_tweets('eu')
    classify_tweets('soamerica')
    classify_tweets('us')
    """
    #process keyword in tweets
    classify_keywords('africa')
    classify_keywords('asia')
    classify_keywords('euro')
    classify_keywords('soamerica')
    classify_keywords('us')
    classify_keywords('total')
