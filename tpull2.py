from TwitterSearch import *
from datetime import datetime
import csv

try:
    #create a TwitterSearch object
    tso = TwitterSearchOrder() 
    #keywords that we want to seach for
    tso.setKeywords(['us education']) 
    #English tweets only
    tso.setLanguage('en') 
    #output 7 results per page
    tso.setCount(7)
    #do not include entity information on output
    tso.setIncludeEntities(False) 
    #reate a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
                       consumer_key = 'NrAPvA9bp9WKgq5MdZHc3ek3M',
                       consumer_secret = 'cHirTdr4jbviiLFJ8fcHiNWsZeoDLuduEzW8apkVKIs2ZaMZQw',
                       access_token = '2422612939-ZgAiq5JR2H39MhWUj8BYSNbIAGkd25WnA4t2CLT',
                       access_token_secret = 'dCwx5NgHHllbyz6FdSowiqy59y3gMZhSCdJ3dAwzbQvcU'
                       )
    #initialize field name for each column
    field = ['tweetid','tweetgeo', 'year', 'text', 'userid', 'usergeo']
    #where search results are initially stored
    data = []
    #counter for how many tweets 
    counter = 0
    #write all the search results in result.txt
    for tweet in ts.searchTweetsIterable(tso):
    	tweetid = tweet['id_str']
    	tweetgeo = None
    	if tweet['coordinates']:
    		tweetgeo = str(tweet['coordinates']['coordinates']) #List
    	year = tweet['created_at'][-4:]
        text = tweet['text'].encode('ascii', 'ignore')
        if text.find('http') != -1:
            text = text[:text.find('http')-1]
        userid = tweet['user']['id_str']
        usergeo = tweet['user']['location'].encode('ascii', 'ignore')
        value = [tweetid, tweetgeo, year, text, userid, usergeo]
        data.append(dict(zip(field, value)))
        counter += 1
    
    #create a file to save search results
    with open('test_output.csv', 'a') as result:
            # create the csv writer object
            time = str(datetime.now())
            print time
            result.write('\nTime of pull: ' + time + '\n')
            tweetwriter = csv.DictWriter(result, delimiter=',', fieldnames=field)
            tweetwriter.writeheader()
            for row in data:
                tweetwriter.writerow(row)

    #print out the total tweets
    print 'Total tweets: '+str(counter)

#throw exception if anything goes wrong
except TwitterSearchException as e:
    print(e)
