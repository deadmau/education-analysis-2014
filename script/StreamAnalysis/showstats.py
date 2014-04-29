import pickle
import operator


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
	withDict = pickle.load(open('../../data/raw/withlocation.pkl', 'rb'))
	withoutSet = pickle.load(open('../../data/raw/withoutlocation.pkl', 'rb'))
	ustSet = pickle.load(open('../../data/cleaned/ustweets.pkl', 'rb'))
	worldtSet = pickle.load(open('../../data/cleaned/worldtweets.pkl', 'rb'))
	totalwDict = pickle.load(open('../../data/cleaned/allwords.pkl', 'rb'))
	uswDict = pickle.load(open('../../data/cleaned/uswords.pkl', 'rb'))
	worldwDict = pickle.load(open('../../data/cleaned/worldwords.pkl', 'rb'))

	print ''
	print ''
	print 'Tweets:'
	print 'Total number of tweets gathered: ' + str(len(withDict) + len(withoutSet))
	print 'Total number of tweets from the US: ' + str(len(ustSet)) 
	print 'Total number of tweets from the rest of the world: ' + str(len(worldtSet))
	print ''
	print 'Words:'
	print 'Total number of adjectives gathered: ' + str(len(totalwDict))
	printTop(totalwDict)
	print ''
	print 'Total number of adjectives gathered from the US: ' + str(len(uswDict))
	printTop(uswDict)
	print ''
	print 'Total number of adjectives gathered from the rest of the world: ' + str(len(worldwDict))
	printTop(worldwDict)
	print ''
		
except BaseException:
	print "One or both files were empty"
	pass
