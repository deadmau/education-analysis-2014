import pickle


def locationAdd(collection):
    try:
        global withDict
        global totalSet
        for tweet in collection:
            if tweet not in withDict:
                withDict[tweet] = collection[tweet]
                if tweet not in totalSet:
                    totalSet.add(tweet)
    except BaseException:
        print "There was an error combining data."
        
        
def nolocationAdd(collection):
    try:
        global totalSet
        for tweet in collection:
            if tweet not in totalSet:
                totalSet.add(tweet)
    except BaseException:
        print "There was an error combining data."


try:
    
    
    withDict = {}
    totalSet = set()
    path = '/Users/Armando_Mota/Desktop/education-analysis-2014/data/raw/'
    armandoDict = pickle.load(open(path + 'armandowithlocation.pkl', 'rb'))
    armandoSet = pickle.load(open(path + 'armandowithoutlocation.pkl', 'rb'))
    elizabethDict = pickle.load(open(path + 'ElizabethWithLocation.pkl', 'rb'))
    elizabethSet = pickle.load(open(path + 'ElizabethWithoutLocation.pkl', 'rb'))
    kiDict = pickle.load(open(path + 'KiWithLocation.pkl', 'rb'))
    kiSet = pickle.load(open(path + 'KiWithoutLocation.pkl', 'rb'))
    #shadmanDict = pickle.load(open(path + 'ShadmanWithLocation.pkl', 'rb'))
    #shadmanSet = pickle.load(open(path + 'ShadmanWithoutLocation.pkl', 'rb'))
    
    locationAdd(armandoDict)
    locationAdd(elizabethDict)
    locationAdd(kiDict)
    #locationAdd(shadmanDict)
    nolocationAdd(armandoSet)
    nolocationAdd(elizabethSet)
    nolocationAdd(kiSet)
    #nolocationAdd(shadmanSet)
    
    locationWrite = open(path + 'locationtweets.pkl', 'wb')
    totalWrite = open(path + 'totaltweets.pkl', 'wb')
    pickle.dump(withDict, locationWrite)
    pickle.dump(totalSet, totalWrite)
    
    print ''
    print "Number of tweets: " + str(len(totalSet))
    
except BaseException:
    print "An error occurred while combining tweet data - please try again."
    pass