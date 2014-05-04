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

if __name__ == '__main__':
    try:
        f = open('../../data/simulated/classifier.pkl', 'rb')
        NBClassifier = pickle.load(f)
        f.close()
    except (OSError, IOError):
        print "File 'classifier.pkl' not found"
        exit(1)
    #process tweets with location
    classify_tweets('africa')
    classify_tweets('asia')
    classify_tweets('eu')
    classify_tweets('soamerica')
    classify_tweets('us')
    """
    #print the final results
    f = open('../../data/simulated/africaAnalyzed.pkl', 'rb')
    df = pickle.load(f)
    f.close()
    print df
    """

