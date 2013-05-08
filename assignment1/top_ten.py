import sys
import json
import operator
from collections import defaultdict

def process_tweets(file):

    ranking = defaultdict(int)

    for line in file:
    	tweet = json.loads(line)
    	if not 'delete' in tweet:
          entities = tweet['entities'] 
          if 'hashtags' in entities:
              if entities['hashtags']:
              	  for hashtag in entities['hashtags']:
                      text = hashtag['text'].lower()
                      ranking[text] +=1
    sort_ranking = sorted(ranking.iteritems(), key= lambda x: x[1], reverse=True) 
    for pos in range(0,10):
        #output = "{0}\t{1}" .format(sort_ranking[pos][0],sort_ranking[pos][1])
        #print output.encode('utf-8')
        word = sort_ranking[pos][0]
        number = float(sort_ranking[pos][1])
        print "%s\t%s" % (word,str(number))

def main():
    tweet_file = open(sys.argv[1])
    process_tweets(tweet_file)

if __name__ == '__main__':
    main()