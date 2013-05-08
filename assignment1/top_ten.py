import sys
import json
import operator

def process_tweets(file):

    ranking = {}
    for line in file:
    	tweet = json.loads(line)
    	if not 'delete' in tweet:
          entities = tweet['entities'] 
          if 'hashtags' in entities:
              if entities['hashtags']:
                  hs =  entities['hashtags'][0]
                  text = hs['text'].lower()
                  if text in ranking:
                      ranking[text] += 1
                  else:
                      ranking[text] = 1  
    sort_ranking = sorted(ranking.iteritems(), key= operator.itemgetter(1), reverse=True)
    for pos in range(0,10):
        print "%s %s" % (sort_ranking[pos][0],sort_ranking[pos][1])

def main():
    tweet_file = open(sys.argv[1])
    process_tweets(tweet_file)

if __name__ == '__main__':
    main()