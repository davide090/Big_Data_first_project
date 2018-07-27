#!/usr/bin/python3

"""mapper.py"""

import sys
import csv
import datetime
from string import punctuation


columns = ["Id","ProductId","UserId","ProfileName","HelpfulnessNumerator","HelpfulnessDenominator",
           "Score","Time","Summary","Text"]

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

sys.stdin.readline()

# input comes from STDIN (standard input)
for words in csv.reader(sys.stdin, delimiter=','):

    # split the line into words
    #words = line.split(",")
    
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    # tab-delimited; the trivial word count is 1
    summary = strip_punctuation(words[8]).lower()
    year = datetime.datetime.fromtimestamp(int(words[7])).strftime('%Y')
    print('%s\t%s' % (year, summary))
