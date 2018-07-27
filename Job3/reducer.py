#!/usr/bin/python3

import sys
#from sortedcontainers import SortedSet
import itertools

current_key = None
key = None
curr_prods = []

def emit_result():
	curr_prods_unique = sorted(curr_prods)
	for pair_prod in itertools.combinations(curr_prods_unique, 2):
		print('{}\t{}'.format(pair_prod, 1))
		#if pair_prod[0] != pair_prod[1]:
			#pair_prod = pair_prod.split()
			#print('{}\t{}'.format(pair_prod, 1))

# user1 [prod1, prod2]
for line in sys.stdin:
	line = line.strip()

	key, prod = line.split('\t')
	#key = key.split()

	if current_key == key:
		curr_prods.append(prod)
	else:
		if current_key == None:
			# prima chiave in assoluto
			current_key = key
			curr_prods.append(prod)
		else:
			# fine lettura chiave corrente
			# emit roba corrente
			#curr_prods_unique = set(curr_prods)
			emit_result();

			current_key = key
			curr_prods = []
			curr_prods.append(prod)

emit_result();
