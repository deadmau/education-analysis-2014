import csv
from string import ascii_letters

#Read the sentiment file and return a dictionary containing the sentiment 
#score of each word, a value from -1 to +1.
def load_sentiments(file_name="sentiments.csv"):
    sentiments = {}
    with open(file_name, 'rU') as result:
        for line in result:
            word, score = line.split(',')
            sentiments[word] = float(score.strip())
    return sentiments

#dictionary for sentiment value
sentiments = load_sentiments()

#Return the words in a tweet, not including punctuation.
def extract_words(text):
    for word in text:
        if word == '.' or word == '\'':
            b = text.replace(word, ' ')
            text = b
        elif word not in ascii_letters and word != ' ':
            b = text.replace(word, ' ')
            text = b
    return text.split()

#Return a sentiment representing the degree of positive or negative
#sentiment in the given tweet, averaging over all the words in the tweet
#that have a sentiment value.
#If none of words have a sentiment value, return 0.
def analyze_text(text):
    words = extract_words(text)
    sentiment_word = 0
    value = 0
    for word in words:
        num = sentiments.get(word, 0)
        if num != 0:
            sentiment_word += 1
            value += num
    if sentiment_word == 0:
        return str(0)
    else:
        return str(value / sentiment_word)

#initialize fields for each column
field = ['year', 'sentiment', 'city']
data = []
try:
    #read twitter_sentiment field by each line
    with open("twitter_sentiment.csv", 'rU') as tweet:
        reader = csv.DictReader(tweet, delimiter=',')
        for line in reader:
            value = [line['year'], analyze_text(line['text']), line['city']]
            data.append(dict(zip(field, value)))

    #create a file to save sentiment results
    with open('twitter_value.csv', 'a') as result:
        # create the csv writer object
        writer = csv.DictWriter(result, delimiter=',', fieldnames=field)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

except IOError as e:
    print "File 'twitter_sentiment.csv' not found"
