#!/usr/bin/python3

"""mapper.py"""

import sys
import csv
import datetime



columns = ["Id","ProductId","UserId","ProfileName","HelpfulnessNumerator","HelpfulnessDenominator",
           "Score","Time","Summary","Text"]

sys.stdin.readline()

# input comes from STDIN (standard input)
for words in csv.reader(sys.stdin, delimiter=','):

    # split the line into words
    #words = line.split(",")
    
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    # tab-delimited; the trivial word count is 1
    userID = str(words[2])
    product= str(words[1])
    if not('#' in userID):
    	print('%s\t%s' % (userID, product))
