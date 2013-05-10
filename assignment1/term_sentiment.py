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
    try:
        if word == 'rt':
            return False
        if word[0] == '@':
            return False
        if word[0] == '#':
            return False
    except:
        return False
    return True

def clean_word(word):
    #word = word.lower()
    word = word.replace(".","")
    word = word.replace(",","")
    return word

def add_new_terms(new_terms_index,tweet_info):

    new_terms = tweet_info['bad_words']
    value_for_new_term = tweet_info['value']
    for term in new_terms:
        if term in new_terms_index:
            values = new_terms_index[term]
            values.append(value_for_new_term)
            new_terms_index[term] = values
        else:
            new_terms_index[term] = [value_for_new_term]

    return new_terms_index    

def calculate_sentiment(text,index):
    my_words = []
    my_bad_words = []
    result = {}

    #print "\n\n[] TWEET []"
    #print "Tweet: ",
    #print text.encode('utf-8')

    try: 
        total = 0
        words = str.split(str(text))

        for word in words:

            #word = clean_word(word)            
            #if good_word(word):
            try: 
                total = total + int(index[word])
                my_words.append(word)
            except KeyError:
                my_bad_words.append(word)
            except ValueError:
                my_bad_words.append(word)
    except UnicodeEncodeError:
        total = 0

    result['value'] = int(total)
    
    if total != 0:
        result['good_words'] = my_words
        result['bad_words'] = my_bad_words
    return result

def generate_output(my_term_index):
    for term in my_term_index:
        values = my_term_index[term]
        values = float(sum(values)) / float(len(values))
        my_term_index[term] = float(values)    
        print "%s %s" % (term,values)

def process_tweets(file,index):
    i = 0
    my_term_index = {}
    tweet_sentiment_info = {}
    
    for line in file:
        data = json.loads(line)
        tweet_sentiment_info = {}
        if not 'delete' in data:
            text = data['text']
            tweet_sentiment_info = calculate_sentiment(text,index)
            if tweet_sentiment_info['value'] != 0:
                my_term_index = add_new_terms(my_term_index, tweet_sentiment_info)
    
    generate_output(my_term_index)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    index = load_dict(sent_file)
    process_tweets(tweet_file,index)

if __name__ == '__main__':
    main()
