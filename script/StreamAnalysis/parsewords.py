from twython import TwythonStreamer
from string import ascii_letters
import pickle, nltk
import csv



totalSet = set()
usSet = set()
euSet = set()
asiaSet = set()
africaSet = set()
soamericaSet = set()

totalWords = {}
usWords = {}
euWords = {}
asiaWords = {}
africaWords = {}
soamericaWords = {}

wordType = ['JJ', 'JJR', 'JJS'] #list for types of adjectives we are going to filter
path = '/Users/Armando_Mota/Desktop/education-analysis-2014/data/cleaned/'
totalFName = path + 'totaltweets.pkl'
usFName = path + 'ustweets.pkl'
euFName = path + 'eutweets.pkl'
asiaFName = path + 'asiatweets.pkl'
africaFName = path + 'africatweets.pkl'
soamericaFName = path + 'soamericatweets.pkl'



# Load all tweets that didn't have location data, all US tweets, and all tweets from the
# rest of the world
def loadFiles():
    global totalSet
    global usSet
    global euSet
    global asiaSet
    global africaSet
    global soamericaSet
    try:
        totalFile = open(totalFName, 'rb')
        usFile = open(usFName, 'rb')
        euFile = open(euFName, 'rb')
        asiaFile = open(asiaFName, 'rb')
        africaFile = open(africaFName, 'rb')
        soamericaFile = open(soamericaFName, 'rb')
        
        totalSet = pickle.load(totalFile)
        totalFile.close()
        usSet = pickle.load(usFile)
        usFile.close()
        euSet = pickle.load(euFile)
        euFile.close()
        asiaSet = pickle.load(asiaFile)
        asiaFile.close()
        africaSet = pickle.load(africaFile)
        africaFile.close()
        soamericaSet = pickle.load(soamericaFile)
        soamericaFile.close()

    except BaseException:
        print "One or more files were empty"
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
def parseWords(setnum):
    global usWords
    global euWords
    global asiaWords
    global africaWords
    global soamericaWords
    global totalWords
    global wordType
    if setnum == 1:
        curwords = usWords
        curset = usSet
    elif setnum == 2:
        curwords = euWords
        curset = euSet
    elif setnum == 3:
        curwords = asiaWords
        curset = asiaSet
    elif setnum == 4:
        curwords = africaWords
        curset = africaSet
    elif setnum == 5:
        curwords = soamericaWords
        curset = soamericaSet
    else:
        curwords = totalWords
        curset = totalSet
        
    for tweet in curset:
        tokens = nltk.word_tokenize(refine_text(tweet).lower())
        tokentext = nltk.Text(tokens)
        tags = nltk.pos_tag(tokentext)
        for wordPair in tags:
            word = wordPair[0]
            # Make sure it's an adjective
            if wordPair[1] in wordType:
                if word in curwords:
                    curwords[word] += 1
                else:
                    curwords[word] = 1


def writeFile(filename, words):
    writer = csv.writer(open(filename + '.csv', 'wb'), delimiter=':')
    for key, value in words.items():
        writer.writerow([key, value])
        pickle.dump(words, open(filename + '.pkl', 'wb'))
    
    

try :
    # Load and parse
    loadFiles()
    parseWords(1) # US
    parseWords(2) # europe
    parseWords(3) # asia
    parseWords(4) # africa
    parseWords(5) # south and central america
    parseWords(6) # all tweets

    # Write
    writeFile(path + 'totalwords', totalWords)
    writeFile(path + 'uswords', usWords)
    writeFile(path + 'euwords', euWords)
    writeFile(path + 'asiawords', asiaWords)
    writeFile(path + 'africawords', africaWords)
    writeFile(path + 'soamericawords', soamericaWords)

    # Notify us of what's happened
    print ''
    print 'There are ' + str(len(totalWords)) + ' distinct adjectives in the total tweet set.'
    print 'There are ' + str(len(usWords)) + ' distinct adjectives in the US tweet set.'
    print 'There are ' + str(len(euWords)) + ' distinct adjectives in the europe tweet set.'
    print 'There are ' + str(len(asiaWords)) + ' distinct adjectives in the asia tweet set.'
    print 'There are ' + str(len(africaWords)) + ' distinct adjectives in the africa tweet set.'
    print 'There are ' + str(len(soamericaWords)) + ' distinct adjectives in the south america tweet set.'
    print ''
except BaseException:
    print "There was an error - please check your files and try again."
    
    
    
