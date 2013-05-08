import sys
import json
import operator
from collections import defaultdict
from collections import Counter

def process_tweets(file):
    lista = []
    ranking = defaultdict(int)
    for line in file:
    	tweet = json.loads(line)
    	if not 'delete' in tweet:
          entities = tweet['entities'] 
          if 'hashtags' in entities:
              if entities['hashtags']:
              	  for hashtag in entities['hashtags']:
                      #text = hashtag['text'].lower()
                      text = hashtag['text']
                      lista.append(hashtag['text'])
                      #ranking[text] += 1.0
    c = Counter(lista)
    top_tags = sorted(c.items(), key = lambda x: x[1], reverse=True)
    #sort_ranking = sorted(ranking.iteritems(), key= lambda x: x[1], reverse=True) 
    for pos in range(0,10):
        output = "{0}\t{1}" .format(top_tags[pos][0],top_tags[pos][1])
        print output.encode('utf-8')
        #word = sort_ranking[pos][0]
        #number = float(sort_ranking[pos][1])
        #print "%s\t%s" % (word,str(number))

def main():
    tweet_file = open(sys.argv[1])
    process_tweets(tweet_file)

if __name__ == '__main__':
    main()