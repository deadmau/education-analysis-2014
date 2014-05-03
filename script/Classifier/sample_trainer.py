#import feature, csv, nltk, nltk.classify
import nltk, csv
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

if __name__ == '__main__': 
    #Read the tweets one by one and process it
    inpTweets = csv.reader(open('../../data/raw/training_dataset.csv', 'rU'), delimiter=',', quotechar='|')
    stopWords = getStopWordList('../../data/raw/stopwords.txt')
    featureList = []
 
    # Get tweet words
    tweets = []
    for row in inpTweets:
        try:
            sentiment = row[0]
            tweet = row[1]
            processedTweet = processTweet(tweet)
            featureVector = getFeatureVector(processedTweet, stopWords)
            featureList.extend(featureVector)
            tweets.append((featureVector, sentiment))
        except IndexError:
            continue
    #end loop
 
    # Remove featureList duplicates and store featureList
    featureList = list(set(featureList))
    f = open('../../data/simulated/featureList.pkl', 'wb')
    pickle.dump(featureList, f)
    f.close()
 
    # Extract feature vector for all tweets in one shote
    training_set = nltk.classify.util.apply_features(extract_features, tweets)

    # Train the classifier
    NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
    
    #store classifier
    f = open('../../data/simulated/classifier.pkl', 'wb')
    pickle.dump(NBClassifier, f)
    f.close()
