import pickle


leftUS = -125.0011
rightUS = -66.9326
topUS = 49.5904
bottomUS = 24.9493

# Australia AU, New Zealand NZ, and Canada CA are being left out for now because I don't know where to put them
# Antarctica  AQ is being included in Europe
europe = set(['AL', 'AD', 'AQ', 'AT', 'AU', 'BY', 'BE', 'BA', 'BG', 'HR', 'CA', 'CY', 'CZ', 'DK', 'ER', 'EE',
	'FO', 'FI', 'FR', 'FX', 'TF', 'DE', 'GI', 'GR', 'GL', 'GD', 'GP', 'VA', 'HU', 'IS', 'IE',
	'IT', 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC', 'ME', 'NL', 'NZ', 'AN', 'NO', 'PL', 'PT',
	'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'TR', 'UA', 'GB', 'XK'])
	
	
asia = set(['AF', 'AS', 'AM', 'AZ', 'BH', 'BD', 'BT', 'IO', 'BN', 'KH', 'CN', 'CK', 'FJ', 
	'PF', 'GE', 'GU', 'HK', 'IN', 'ID', 'IR', 'IQ', 'IL', 'JP', 'JO', 'KZ', 'KP', 'KR', 'KW',
	'KG', 'LA', 'LB', 'MO', 'MG', 'MY', 'MV', 'MH', 'FM', 'MN', 'MM', 'NP', 'MP', 'PK', 'PW', 
	'PG', 'PH', 'WS', 'SA', 'SB', 'SG', 'GS', 'LK', 'SR', 'SY', 'TW', 'TJ', 'TH', 'TO','TM', 'TV',
	'AE', 'UZ', 'VN'])
	
	
africa = set(['DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'BI', 'CM', 'CV', 'CF', 'TD', 'CG', 'CD',
	'CI', 'DJ', 'DG', 'GQ', 'EG', 'ET', 'GF', 'GA', 'GM', 'GH', 'GN', 'GW', 'GY', 'KE', 'LS', 'LR',
	'LY', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA',  'NE', 'NG', 'OM', 'QA', 'RW', 'SN', 'SL',
	'SO', 'ZA', 'SS', 'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'EH', 'YE', 'ZM', 'ZW'])
	
	
soamerica = set(['AI', 'AG', 'AR', 'AW', 'BS', 'BB', 'BZ', 'BM', 'BO', 'BR', 'KY', 'CL', 'CO', 'CR',
	'CU', 'DO', 'EC', 'SV', 'FK', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MX', 'NI', 'PA', 'PY', 'PE',
	'PR', 'KN', 'LC', 'TT', 'TC', 'UY', 'VC', 'VE', 'VG', 'VI'])
	

locText = {}
usSet = set()
totalCorrupt = 0;
totalCount = 0;
#worldSet = set()
euSet = set()
asiaSet = set()
africaSet = set()
soamericaSet = set()

readpath = '/Users/Armando_Mota/Desktop/education-analysis-2014/data/raw/'
writepath = '/Users/Armando_Mota/Desktop/education-analysis-2014/data/cleaned/'
locationFile = readpath + 'locationtweets.pkl'
usFile = writepath + 'ustweets.pkl'
#worldFile = 'worldtweets.pkl'
euroFile = writepath + 'eutweets.pkl'
asiaFile = writepath + 'asiatweets.pkl'
africaFile = writepath + 'africatweets.pkl'
soamericaFile = writepath + 'soamericatweets.pkl'


def loadFile(file1):
    global locText
    try:
        locFile = open(file1, 'rb')
        locText = pickle.load(locFile)
        locFile.close()
    except BaseException:
        print "The dictionary in " + totalFile + "couldn't be accessed"
        return


def findCountry(place):
    global locText
    # tweet has country code
    if isinstance(place, str):
        if place == "US":
            return 1
        # outside US
        elif place in europe:
        	return 2
        elif place in asia:
        	return 3
        elif place in africa:
        	return 4
        elif place in soamerica:
        	return 5
        else:
        	#print "Country code " + place + " is not in our list of countries."
        	return 6
             
    # tweet has lat/long coordinates but no country code
    else:
        lat = place[0]
        long = place[1]
        # in US
        if lat > leftUS and lat < rightUS and long > bottomUS and long < topUS:
            return 1
        # outside US
        else:
            #print "Lat/long codes outside of the US!"
            return 6
        
        
        
try :
    #open files to write to
    loadFile(locationFile)
    usWrite = open(usFile, 'wb')
    euWrite = open(euroFile, 'wb')
    asiaWrite = open(asiaFile, 'wb')
    africaWrite = open(africaFile, 'wb')
    soamericaWrite = open(soamericaFile, 'wb')
          
    #fill sets with appropriate tweets
    for tweet in locText:
        place = locText[tweet]
        country = findCountry(place)
        if country == 1:
            usSet.add(tweet)
        elif country == 2:
            euSet.add(tweet)
    	elif country == 3:
    		asiaSet.add(tweet)
    	elif country == 4:
    		africaSet.add(tweet)
    	elif country == 5:
    		soamericaSet.add(tweet)
    	else:
    		totalCount -= 1
    		totalCorrupt += 1
    	totalCount += 1
    		
    
    #write to files
    pickle.dump(usSet, usWrite)
    pickle.dump(euSet, euWrite)
    pickle.dump(asiaSet, asiaWrite)
    pickle.dump(africaSet, africaWrite)
    pickle.dump(soamericaSet, soamericaWrite)
    usWrite.close()
    euWrite.close()
    asiaWrite.close()
    africaWrite.close()
    soamericaWrite.close()
    print "Number of tweets with location data: " + str(totalCount)
    print "Number of tweets excluded for containing bad/improper data: " + str(totalCorrupt)
    print ''

except BaseException:
    print "There was an error opening and parsing the files"

    