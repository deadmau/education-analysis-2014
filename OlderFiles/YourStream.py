from twython import TwythonStreamer
import pickle



# set up keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# set up set and dictionary to locally store tweets and words until external file save
textSet = set()
wordDict = {}

# load previous set/dictionary data into textSet and wordDict if they exist
def loadFiles():
    try:
        textFile = open('YourNameTexts.pkl', 'rb')
        wordFile = open('YourNameWords.pkl', 'rb')
        textSet = pickle.load(textFile)
        wordDict = pickle.load(wordFile)
        textFile.close()
        wordFile.close()
    except BaseException:
        print "One or both files were empty"
        pass

# makes the magic happen
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            text = data['text'].encode('utf-8')
            if text.find('http') != -1:
                text = text[:text.find('http')-1]
            words = text.split()
            if text not in textSet:
                textSet.add(text)
                for word in words:
                    if word in wordDict:
                        wordDict[word] += 1
                    else:
                        wordDict[word] = 1
            
    def on_error(self, status_code, data):
        print status_code
        self.disconnect()


# run it
try :
    loadFiles()
    textWrite = open('YourNameTexts.pkl', 'wb')
    wordWrite = open('YourNameWords.pkl', 'wb')      
    stream = MyStreamer(consumer_key, consumer_secret, access_token, access_token_secret)
    # this line actually starts the streaming, with college as the keyword
    stream.statuses.filter(track='college')
except (KeyboardInterrupt, SystemExit):
	# when you hit Ctrl^C, this catches the exception and writes everything that has been
	# added to the set and dictionary to the two files specified above.  YOU MUST ONLY STOP
	#THIS SCRIPT WITH CTRL^C OR ELSE YOU WON'T SAVE ANY OF THE DATA YOU'VE COLLECTED IN THE
	#CURRENT SESSION
	pickle.dump(textSet, textWrite)
	pickle.dump(wordDict, wordWrite)