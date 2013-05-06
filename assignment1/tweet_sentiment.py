import sys
import json
import re

def load_dict(file):
    index = {}
    for line in file:
        line_data = str.split(str(line))
        index[line_data[0]] = line_data[1]
    return index

def good_word(word):
    
    if word == 'RT':
        return False
    if word[0] == '@':
        return False
    return True

def calculate_sentiment(text,index):
    try: 
        total = 0
        words = str.split(str(text))
        errors = 0    
        #print "\n\n[] TWEET []\n"    
        #print "Tweet: ",
        #print text.encode('utf-8'),

        for word in words:
            #print word,
            if good_word(word):
                try: 
                    total = total + int(index[word])
                except KeyError:
                    errors += 1
                except ValueError:
                    errors += 1
            else:
                errors += 1
    
    except UnicodeEncodeError:
        total = 0

    # print " Sentiment Value = %s" % str(total)
    return total

def process_tweets(file,index):
    i = 0
    for line in file:
        data = json.loads(line)
        if not 'delete' in data:
            text = data['text']
            value = calculate_sentiment(text,index)
            print value
        i += 1
        if i == 100:
            break

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    index = load_dict(sent_file)
    process_tweets(tweet_file,index)

if __name__ == '__main__':
    main()
