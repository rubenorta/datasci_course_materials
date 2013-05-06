import sys
import json
import re


def calculate_frequency(text,index):
    try:
    	  words = str.split(str(text))
    	  for word in words:
    	  	  if word in index:
    	  	  	  index[word] = index[word] + 1
    	  	  else:
    	  	  	  index[word] = 1
    	  	  index['correct_words'] += 1 
    except UnicodeEncodeError:
    	  index['error_tweets'] += 1
    return index

def process_tweets(file):

    index = {'error_tweets' : 0 , 'correct_words' : 0}  
    for line in file:
        data = json.loads(line)
        if not 'delete' in data:
            text = data['text']
            index = calculate_frequency(text,index)
            #print text
    for term in index:
    	if term != 'error_tweets' and term != 'correct_words':
    		frequency = float(index[term]) / float(index['correct_words'])
    		print "%s %s" % (term,str(frequency))

    #print index
    #print "OK Tweets %s ERROR Tweets %s" % (index['correct_words'],index['error_tweets'])

def main():
    tweet_file = open(sys.argv[1])
    process_tweets(tweet_file)

if __name__ == '__main__':
    main()
