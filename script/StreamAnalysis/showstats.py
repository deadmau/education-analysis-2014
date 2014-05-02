import pickle
import operator

path = '../../data/cleaned/'

def printTop(wordDict):
    try:
        sortedWords = sorted(wordDict.iteritems(), key=operator.itemgetter(1))
        sortedWords.reverse()
        i = 0
        print '   The top 10 are:'
        while i < 10 and i < len(sortedWords):
        	print '      ' + sortedWords[i][0] + ', ' + str(sortedWords[i][1]) + ' times'
        	i += 1
    except BaseException:
        print "There was an error passing the dictionary"
        pass


try:
	
	totaltDict = pickle.load(open(path + 'totaltweets.pkl', 'rb'))
	ustSet = pickle.load(open(path + 'ustweets.pkl', 'rb'))
	eutSet = pickle.load(open(path + 'eutweets.pkl', 'rb'))
	asiatSet = pickle.load(open(path + 'asiatweets.pkl', 'rb'))
	africatSet = pickle.load(open(path + 'africatweets.pkl', 'rb'))
	soamericatSet = pickle.load(open(path + 'soamericatweets.pkl', 'rb'))
	
	totalwDict = pickle.load(open(path + 'totalwords.pkl', 'rb'))
	uswDict = pickle.load(open(path + 'uswords.pkl', 'rb'))
	euwDict = pickle.load(open(path + 'euwords.pkl', 'rb'))
	asiawDict = pickle.load(open(path + 'asiawords.pkl', 'rb'))
	africawDict = pickle.load(open(path + 'africawords.pkl', 'rb'))
	soamericawDict = pickle.load(open(path + 'soamericawords.pkl', 'rb'))

	print ''
	print ''
	print 'Tweets:'
	print 'Total number of tweets gathered: ' + str(len(totaltDict))
	print 'Total number of tweets from the US: ' + str(len(ustSet)) 
	print 'Total number of tweets from europe: ' + str(len(eutSet)) 
	print 'Total number of tweets from asia: ' + str(len(asiatSet)) 
	print 'Total number of tweets from africa: ' + str(len(africatSet)) 
	print 'Total number of tweets from south and central america: ' + str(len(soamericatSet)) 
	print ''
	print 'Words:'
	print 'Total number of distinct adjectives gathered: ' + str(len(totalwDict))
	print 'Total number of distinct adjectives gathered from the US: ' + str(len(uswDict))
	print 'Total number of distinct adjectives gathered from europe: ' + str(len(euwDict))
	print 'Total number of distinct adjectives gathered from asia: ' + str(len(asiawDict))
	print 'Total number of distinct adjectives gathered from africa: ' + str(len(africawDict))
	print 'Total number of distinct adjectives gathered from south and central america: ' + str(len(soamericawDict))
	print ''
		
except BaseException:
	print "One or both files were empty"
	pass
