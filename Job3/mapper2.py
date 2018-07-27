#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	key, value = line.split('\t')
	key = key.split()

	print('{}\t{}'.format(key, value))
