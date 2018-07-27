#!/usr/bin/python3
import sys
import time


# maps words to their counts
text2year = {}
 

def mostFrequent(stringa):
    
    word2count = {}
    
    for word in stringa.split(" "):
        try:
            word2count[word] = word2count[word]+1
        except:
            word2count[word] = 1
            
    sorted_by_value = sorted(word2count.items(), key=lambda x:x[1])
    sorted_by_value.reverse()
    
    return sorted_by_value[:10]


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
 
    # parse the input we got from mapper.py
    try:
        year,text = line.split('\t')
    except:
        continue

    try:
        text2year[year] = text2year[year] + " " + text
    except:
        text2year[year] = text
 

 # write the tuples to stdout
for year in text2year.keys():
    words_freq = mostFrequent(text2year[year])
    
    print ('%s\t%s' % (year, words_freq) )

