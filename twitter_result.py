from TwitterSearch import *
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

    #create a file to save search results
    result = open('twitter_sentiment.txt', 'w+')
    #counter for how many tweets 
    counter = 0
    #write all the search results in result.txt
    for tweet in ts.searchTweetsIterable(tso):
        result.write( '%s \t %s \t %s \n' % ( tweet['user']['created_at'].encode('ascii', 'ignore'), tweet['text'].encode('ascii', 'ignore'), tweet['user']['location'].encode('ascii', 'ignore')) )
        counter += 1
    result.write('Total tweets: '+str(counter))
    #close file
    result.close()

#throw exception if anything goes wrong
except TwitterSearchException as e:
    print(e)
