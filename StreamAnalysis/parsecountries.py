import pickle


leftUS = -125.0011
rightUS = -66.9326
topUS = 49.5904
bottomUS = 24.9493
locText = {}
usSet = set()
worldSet = set()
totalFile = 'withlocation.pkl'
usFile = 'ustweets.pkl'
worldFile = 'worldtweets.pkl'


def loadFile(file1):
    global locText
    try:
        locFile = open(file1, 'rb')
        locText = pickle.load(locFile)
        locFile.close()
    except BaseException:
        print "The dictionary in " + totalFile + "couldn't be accessed"
        return


def inUS(place):
    global locText
    # tweet has country code
    if isinstance(place, str):
        if place == "US":
            return True
        # outside US
        else:
            return False
    # tweet has lat/long coordinates but no country code
    else:
        lat = place[0]
        long = place[1]
        # in US
        if lat > leftUS and lat < rightUS and long > bottomUS and long < topUS:
            return True
        # outside US
        else:
            return False
        
        
        
try :
    #open files to write to
    loadFile(totalFile)
    usWrite = open(usFile, 'wb')
    worldWrite = open(worldFile, 'wb')
          
    #fill sets with appropriate tweets
    #print locText
    for tweet in locText:
        place = locText[tweet]
        if inUS(place):
            usSet.add(tweet)
        else:
            worldSet.add(tweet)
    
    #write to files
    pickle.dump(usSet, usWrite)
    pickle.dump(worldSet, worldWrite)
    usWrite.close()
    worldWrite.close()
    print ''
    print "Total number of tweets with location data: " + str(len(locText))
    print 'Total number of tweets in the US: ' + str(len(usSet)) 
    print 'Total number of tweets in the rest of the world: ' + str(len(worldSet))
    print ''
except BaseException:
    print "There was an error opening the file(s)"
    