import sys
import json
import pprint


def load_dict(file):
    index = {}
    for line in file:
        line_data = str.split(str(line))
        index[line_data[0]] = line_data[1]
    return index

def get_sentiment(tweet, index):
    try:
        total = 0
        words = text.encode("utf-8").split()
        for word in words:
            if word in index:
                total = total + int(index[word])
    except UnicodeEncodeError:
	    total = 0
    return total

def get_state(tweet):
    pos = 'place'
    if pos in tweet:
	    tweet_place = tweet['place']
        country = tweet_place['country_code']
        if country == 'US':
            state_code = place['full_name'][-2::]
            print place['full_name']
            print state_code
    return state_code

def process_tweets(file,index):
    i = 0
    for line in file:
    	  tweet = json.loads(line)
    	  if not 'delete' in tweet:
    	  	  sentiment = get_sentiment(tweet,index)
    	  	  state_code = get_state(tweet)
    	  	  print "%s %s %s" % (sentiment, state_code, tweet['text'])
        	  i += 1
        	  if i == 1000:
        	      break
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    index = load_dict(sent_file)
    process_tweets(tweet_file,index)

if __name__ == '__main__':
    main()
