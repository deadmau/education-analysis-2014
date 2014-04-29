Package details:



allwords.pkl: Pickle file containing all adjectives and their frequencies
	
parsecountries.py: This splits the tweets from withlocation.pkl into ustweets.pkl if they 
	are from the US, and worldtweets.pkl if they aren't
	
parsewords.py: This script parses words out of the files ustweets.pkl, worldtweets.pkl, and
	withoutlocation.pkl (all tweets collected).  It places the words and their frequencies
	in three files: allwords.pkl for all tweets, uswords.pkl for just US tweets, and
	worldwords.pkl for tweets outside of the US.
	**NOTE**: This may take a long time to run, so let it run, it's not frozen.
	
showstats.py: This displays all of your current stats in the terminal.  It displays:
	Total number of tweets gathered
	Total number of tweets from the US
	Total number of tweets from outside the US
	Total number of adjectives gathered
	Top 20 adjectives overall
	Total number of adjectives gathered from US
	Top 20 adjectives from US
	Total number of adjectives gathered from outside the US
	Top 20 adjectives from outside the US
	
stream.py: This is the main file - run this to stream twitter data and store it in 
	the files withlocation.pkl (if the tweet has location data) and withoutlocation.pkl (if
	the file doesn't have location data).  REMEMBER: You must exit this script by using
	ctrl^C - if you don't, none of the data you've collected in that session will be saved,
	and furthermore all of your previous data will be erased as well.
	
ustweets.pkl: Pickle file containing all tweets from the US

uswords.pkl: Pickle file containing all adjectives from the US and their frequencies

withlocation.pkl: Pickle file containing all tweets that have locations, and their locations

withoutlocation.pkl: Pickle file containing all tweets that don't have location data

worldtweets.pkl: Pickle file containing all tweets from outside the US

worldwords.pkl: Pickle file containing all adjectives from outside the US and their frequencies


STANDARD USAGE FLOW:
	Run:
		python stream.py (every time you want to gather more tweets)
		
		python parsecountries.py (when you want to split tweets into US and outside US)
		
		python parsewords.py (when you want to split words into frequencies for overall,
			just US, and rest of the world)
		
		python showstats.py (when you want to view what you've done so far)
		
		
		
		You can run all of these files as often as you want.  stream.py continually adds
		new tweets to what it currently had, and the other three files do their processes
		from scratch every time so you can run them whenever and how often you like.
		
		