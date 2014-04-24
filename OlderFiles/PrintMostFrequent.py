import pickle
import operator


def printTopTwenty():
    try:
        wordFile = open('YourNameWords.pkl', 'rb')
        wordDict = pickle.load(wordFile)
        wordFile.close()
        sortedWords = sorted(wordDict.iteritems(), key=operator.itemgetter(1))
        sortedWords.reverse()
        print "The 20 most frequent words that appear with college are:"
        i = 0
        while i < 20:
        	print sortedWords[i][0] + ', ' + str(sortedWords[i][1]) + ' times'
        	i += 1
    except BaseException:
        print "There was an error loading the file"
        pass


printTopTwenty()