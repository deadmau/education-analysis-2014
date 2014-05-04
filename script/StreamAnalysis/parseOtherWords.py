import pickle



words = ['cost', 'quality', 'time', 'benefit'] # This list can change if we want to add/subtract
continents = ['total', 'US', 'europe', 'asia', 'africa', 'south/central america']
path = '/Users/Armando_Mota/Desktop/education-analysis-2014/data/cleaned/'
# These will hold the initially loaded tweet data
totalSet = set()
usSet = set()
euroSet = set()
asiaSet = set()
africaSet = set()
soamericaSet = set()
tweetArray = []
# These will become arrays of sets when they're filled with data
totalWords = {'cost':set(), 'quality':set(), 'time':set(), 'benefit':set()}
usWords = {'cost':set(), 'quality':set(), 'time':set(), 'benefit':set()}
euroWords = {'cost':set(), 'quality':set(), 'time':set(), 'benefit':set()}
asiaWords = {'cost':set(), 'quality':set(), 'time':set(), 'benefit':set()}
africaWords = {'cost':set(), 'quality':set(), 'time':set(), 'benefit':set()}
soamericaWords = {'cost':set(), 'quality':set(), 'time':set(), 'benefit':set()}
tweetbywordArray = [totalWords, usWords, euroWords, asiaWords, africaWords, soamericaWords]




def openFiles():
    try:
    	global totalSet
        global usSet
        global euroSet
        global asiaSet
        global africaSet
        global soamericaSet
        global tweetArray
        totalSet = pickle.load(open(path + 'totaltweets.pkl', 'rb'))
        usSet = pickle.load(open(path + 'ustweets.pkl', 'rb'))
        euroSet = pickle.load(open(path + 'eutweets.pkl', 'rb'))
        asiaSet = pickle.load(open(path + 'asiatweets.pkl', 'rb'))
        africaSet = pickle.load(open(path + 'africatweets.pkl', 'rb'))
        soamericaSet = pickle.load(open(path + 'soamericatweets.pkl', 'rb'))
        tweetArray = [totalSet, usSet, euroSet, asiaSet, africaSet, soamericaSet]
    except BaseException:
        print "There was an error reading data from the files containing tweets."

    

def writeFiles():
    try:
        pickle.dump(totalWords, open(path + 'totalOtherWordTweets.pkl', 'wb'))
        pickle.dump(usWords, open(path + 'usOtherWordTweets.pkl', 'wb'))
        pickle.dump(euroWords, open(path + 'euroOtherWordTweets.pkl', 'wb'))
        pickle.dump(asiaWords, open(path + 'asiaOtherWordTweets.pkl', 'wb'))
        pickle.dump(africaWords, open(path + 'africaOtherWordTweets.pkl', 'wb'))
        pickle.dump(soamericaWords, open(path + 'soamericaOtherWordTweets.pkl', 'wb'))
    except BaseException:
        print "There was an error writing the processed tweet objects to files."



def parseTweetsByWord():
    try:
        global totalSet
        global usSet
        global euroSet
        global asiaSet
        global africaSet
        global soamericaSet
        global tweetArray
        
        global totalWords
        global usWords
        global euroWords
        global asiaWords
        global africaWords
        global soamericaWords
        global tweetbywordArray
        
        for tweetset in tweetArray:
            index = tweetArray.index(tweetset)
            for tweet in tweetset:
                #print tweet
                for word in words:
                    if word in tweet:
                        #print word + ': ' + tweet
                        tweetbywordArray[index][word].add(tweet)

    except BaseException:
        print "There was an error parsing tweets by word."
        
        


# Run it
openFiles()
parseTweetsByWord()
writeFiles()
print ''
print "Tweet by word successful!"
for tweetSet in tweetbywordArray:
	index = tweetbywordArray.index(tweetSet)
	print ''
	for word in words:
		print "Number of " + continents[index] + " tweets containing " + word + ': ' + str(len(tweetSet[word]))
	print ''
