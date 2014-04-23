from tweepy import *
from datetime import datetime
import time
import csv
import json


consumer_key = 'NrAPvA9bp9WKgq5MdZHc3ek3M'
consumer_secret = 'cHirTdr4jbviiLFJ8fcHiNWsZeoDLuduEzW8apkVKIs2ZaMZQw'
access_token = '2422612939-ZgAiq5JR2H39MhWUj8BYSNbIAGkd25WnA4t2CLT'
access_token_secret = 'dCwx5NgHHllbyz6FdSowiqy59y3gMZhSCdJ3dAwzbQvcU'

   
class listener(StreamListener):
    def on_data(self, data):
        try:
            tweetgeo = None
            jsonData = json.loads(data)
            text = jsonData['text'].encode('ascii', 'ignore')
            if text.find('twitter') != -1:
            	print text
            else:
            	print 'Bad tweet'
            return True
            #if jsonData['coordinates']:
            	#tweetgeo = str(jsonData['coordinates']['coordinates'])
            # if text.find('http') != -1:
            #    text = text[:text.find('http')-1]
            #userid = jsonData['user']['id_str'].encode('ascii', 'ignore')
            #usergeo = jsonData['user']['location'].encode('ascii', 'ignore')        
            #writeFile = open('ArmandoOutput.csv', 'a')
            #outwriter = csv.writer(writeFile, delimiter=',')
            #outwriter.writerow([tweetgeo, text, userid, usergeo])
            #writeFile.close()
            #print text
            #return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(300)
            return
            
    def on_error(self, status):
        print status
        twitterStream.disconnect()
        return


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track='twitter') #, locations=[-125.0011, 24.9493, -66.9326, 49.5904], languages=['en'])
    
