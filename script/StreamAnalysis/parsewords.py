from twython import TwythonStreamer
from string import ascii_letters
import pickle, nltk



withoutSet = set()
usSet = set()
worldSet = set()

totalWords = {}
usWords = {}
worldWords = {}

wordType = ['JJ', 'JJR', 'JJS'] #list for types of adjectives we are going to filter
withoutl = '../../data/raw/withoutlocation.pkl'
usl = '../../data/cleaned/ustweets.pkl'
worldl = '../../data/cleaned/worldtweets.pkl'



# Load all tweets that didn't have location data, all US tweets, and all tweets from the
# rest of the world
def loadFiles():
    global withoutSet
    global usSet
    global worldSet
    try:
        withoutFile = open(withoutl, 'rb')
        usFile = open(usl, 'rb')
        worldFile = open(worldl, 'rb')
        withoutSet = pickle.load(withoutFile)
        usSet = pickle.load(usFile)
        worldSet = pickle.load(worldFile)
        withoutFile.close()
        usFile.close()
        worldFile.close()
    except BaseException:
        print "One or both files were empty"
        pass
        

#Refine text in a tweet, not including punctuation.
def refine_text(text):
    for word in text:
        if word == '.' or word == '\'':
            b = text.replace(word, ' ')
            text = b
        elif word not in ascii_letters and word != ' ':
            b = text.replace(word, ' ')
            text = b
    return text
    

# Parse words out from the input set and place tweets in the correct output sets
def parseWords(tweetSet):
	for tweet in tweetSet:
		tokens = nltk.word_tokenize(refine_text(tweet).lower())
		tokentext = nltk.Text(tokens)
		tags = nltk.pos_tag(tokentext)
		for wordPair in tags:
			word = wordPair[0]
			if wordPair[1] in wordType:
				# This is a word whose tweet was located in the US
				if len(tweetSet) == len(usSet):
					if word in usWords:
						usWords[word] += 1
					else:
						usWords[word] = 1
					
				# This is a word whose tweet was located outside the US     
				elif len(tweetSet) == len(worldSet):
					if word in worldWords:
						worldWords[word] += 1
					else:
						worldWords[word] = 1
				
				# Every tweet, regardless of where it came from or whether it had location data,
				# gets added to the total list
				if word in totalWords:
					totalWords[word] += 1
				else:
					totalWords[word] = 1
    
    
    
# run it
try :
    # Load and run
    loadFiles()
    parseWords(withoutSet)
    parseWords(usSet)
    parseWords(worldSet)
    totalWrite = open('../../data/cleaned/allwords.pkl', 'wb')
    usWrite = open('../../data/cleaned/uswords.pkl', 'wb')
    worldWrite = open('../../data/cleaned/worldwords.pkl', 'wb')
    # Write
    pickle.dump(totalWords, totalWrite)
    pickle.dump(usWords, usWrite)
    pickle.dump(worldWords, worldWrite)
    totalWrite.close()
    usWrite.close()
    worldWrite.close()
    # Notify us of what's happened
    print ''
    print 'There are ' + str(len(totalWords)) + ' adjectives in the total tweet set.'
    print 'There are ' + str(len(usWords)) + ' adjectives in the US tweet set.'
    print 'There are ' + str(len(worldWords)) + ' adjectives in the world tweet set.'
    print ''
except BaseException:
    print "There was an error - please check your files and try again."
    
    
    
    
    
    
    
    
    
