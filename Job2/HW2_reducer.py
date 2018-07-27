#!/usr/bin/python3
import sys
import time

# maps year to their scores
product2year_score = {}

#calculate average of scores per year
def average_year(year_score):
    
    result={}
    
    for k,v in year_score.items():
               
        somma = sum(map(float, v))
        count = len(year_score[k])

        result[k]=  str(somma/count)
    
    return result




# input comes from STDIN
for line in sys.stdin:
 
    # parse the input we got from mapper.py
    product, year_score = line.split('\t')
    year, score = year_score.split(':')
    
    if product in product2year_score:
        
        if year in product2year_score[product]:
            
            product2year_score[product][year].append(score)

        else:
            product2year_score[product][year] = [score]

    else:
        product2year_score[product] = {year:[score]}


#sort dictionary by key (product)    
prod2 = (sorted(product2year_score.items()))


#get dict from sorted list of tuples (product, dict)
prod2_dict = dict(prod2)

for k in prod2_dict.keys():
    avg = average_year(prod2_dict[k])
    
    print ('%s\t%s' % (k, avg) )

