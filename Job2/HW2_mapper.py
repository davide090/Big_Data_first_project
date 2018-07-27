#!/usr/bin/python3

"""mapper.py"""

import sys
import csv
import datetime
import time



columns = ["Id","ProductId","UserId","ProfileName","HelpfulnessNumerator","HelpfulnessDenominator",
           "Score","Time","Summary","Text"]

sys.stdin.readline()

# input comes from STDIN (standard input)
for words in csv.reader(sys.stdin, delimiter=','):
    
    year = datetime.datetime.fromtimestamp(int(words[7])).strftime('%Y')
    
    if(int(year) >= 2003 and int(year) <= 2012):
        
        product = words[1]
        score = words[6]
        
        print('%s\t%s:%s' % (product, year, score))
