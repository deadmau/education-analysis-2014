from TwitterSearch import *
import csv

try:
    #create a TwitterSearch object
    tso = TwitterSearchOrder() 
    #keywords that we want to seach for
    tso.setKeywords(['"us education"'+':('+'since:2010-01-01']) 
    #English tweets only
    tso.setLanguage('en') 
    #output 7 results per page
    tso.setCount(7)
    #do not include entity information on output
    tso.setIncludeEntities(False) 
    #reate a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
                       consumer_key = 'uVIphnOOjUHubKdicEkA',
                       consumer_secret = '31VcB8ZIunTkSDWnHyJosEMrkNpNy9ecQigxOMruSk',
                       access_token = '2419638589-5THAmW79kgGzcF3USxmi4kK0KA4UiUBzCMFxI6x',
                       access_token_secret = 'Pkb4ZPHODZ4ucDoKMPtzjbehlffIX6dUj84Yt5UmJbOGU'
                       )
    #initialize field name for each column
    field = ['year', 'text', 'city']
    #where search results are initially stored
    data = []
    #counter for how many tweets 
    counter = 0
    #write all the search results in result.txt
    for tweet in ts.searchTweetsIterable(tso):
        value = [tweet['user']['created_at'][-4:], tweet['text'].encode('ascii', 'ignore'), tweet['user']['location'].encode('ascii', 'ignore')]
        data.append(dict(zip(field, value)))
        counter += 1
    
    #create a file to save search results
    with open('twitter_sentiment.csv', 'w+') as result:
            # create the csv writer object
            tweetwriter = csv.DictWriter(result, delimiter=',', fieldnames=field)
            tweetwriter.writeheader()
            for row in data:
                tweetwriter.writerow(row)

    #print out the total tweets
    print 'Total tweets: '+str(counter)

#throw exception if anything goes wrong
except TwitterSearchException as e:
    print(e)
