import sys
import json
import pprint
import operator

def load_dict(file):
    index = {}
    for line in file:
        line_data = str.split(str(line))
        index[line_data[0]] = line_data[1]
    return index

def get_sentiment(tweet, index):
    try:
        total = 0
        words = tweet['text'].split()
        for word in words:
            if word in index:
                total = total + int(index[word])
    except ValueError:
        total = 0
    except UnicodeEncodeError:
	    total = 0
    return total

def get_state(tweet):

    state_code = ''

    if tweet['place'] != None:
        tweet_place = tweet['place']
        country = tweet_place['country_code']
        if country == 'US':
            state_code = tweet_place['full_name'][-2::]    
    return state_code

def process_tweets(file,index):
    i = 0
    ranking = {}
    for line in file:
    	tweet = json.loads(line)
    	if not 'delete' in tweet:
            state_code = get_state(tweet)
            if state_code != '':
                sentiment = get_sentiment(tweet,index)
                if state_code in ranking:
                    ranking[state_code] += sentiment
                    #print "O %s %s" % (state_code,ranking[state_code])
                else:
                    ranking[state_code] = sentiment
                    #print "N %s %s" % (state_code,ranking[state_code])

    sort_ranking = sorted(ranking.iteritems(), key= operator.itemgetter(1))
    print sort_ranking[len(sort_ranking)-1][0]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    index = load_dict(sent_file)
    process_tweets(tweet_file,index)

if __name__ == '__main__':
    main()
