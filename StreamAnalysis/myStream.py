from twython import TwythonStreamer
import pickle



# set up keys
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# set up set and dictionary to locally store tweets and words until external file save
locText = {}
noLocText = set()
oglocsize = 0
ognolocsize = 0
filename1 = 'WithLocation.pkl'
filename2 = 'WithoutLocation.pkl'


# load previous set/dictionary data into textSet and wordDict if they exist
def loadFiles(file1, file2):
    global locText
    global noLocText
    global oglocsize
    global ognolocsize
    try:
        locFile = open(file1, 'rb')
        noLocFile = open(file2, 'rb')
        locText = pickle.load(locFile)
        noLocText = pickle.load(noLocFile)
        oglocsize = len(locText)
        ognolocsize = len(noLocText)
        locFile.close()
        noLocFile.close()
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
            if text not in locText and text not in noLocText and text.find('college') != -1:
                # print text
                if data['place'] != None:
                    locText[text] = (data['place']['country_code']).encode('ascii','ignore')
                else:
                    if data['coordinates'] != None:
                        locText[text] = data['coordinates']['coordinates']
                    else:
                        noLocText.add(text)
                
            
    def on_error(self, status_code, data):
        print status_code
        self.disconnect()


# run it
try :
    loadFiles(filename1, filename2)
    locWrite = open(filename1, 'wb')
    noLocWrite = open(filename2, 'wb')      
    stream = MyStreamer(consumer_key, consumer_secret, access_token, access_token_secret)
    # this line actually starts the streaming, with college as the keyword
    stream.statuses.filter(track='college')
except (KeyboardInterrupt, SystemExit):
    # when you hit Ctrl^C, this catches the exception and writes everything that has been
    # added to the set and dictionary to the two files specified.  YOU MUST ONLY STOP THIS
    # SCRIPT WITH CTRL^C OR ELSE YOU WON'T SAVE ANY OF THE DATA YOU'VE COLLECTED IN THE
    # CURRENT SESSION
    pickle.dump(locText, locWrite)
    pickle.dump(noLocText, noLocWrite)
    locWrite.close()
    noLocWrite.close()
    print ''
    print ''
    print 'Gathered ' + str(len(locText) - oglocsize) + ' tweets with locations.'
    print 'Gathered ' + str(len(noLocText) - ognolocsize) + ' tweets with no locations.'
    print ''
