#!/usr/bin/python3

import sys
import collections
import itertools

current_key = None
key = None
current_count = []

def emit_result():
	print('{}\t{}'.format(current_key, len(current_count)))


for line in sys.stdin:
	line = line.strip()

	key, count = line.split('\t')
	#key = key.split()

	try:
		count = int(count)
	except ValueError:
		continue

	if current_key == key:
		current_count.append(count)
	else:
		if current_key == None:
			current_key = key
			current_count = [count]
		else:
			emit_result()
			
			current_key = key
			current_count = [count]
emit_result()
