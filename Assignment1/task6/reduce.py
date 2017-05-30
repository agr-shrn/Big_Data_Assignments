#!/usr/bin/env python

import csv
import os
import sys
import collections

currentkey = None
count = 0
max = 0
violations = {}

for line in sys.stdin:

	line = line.strip()
	key, value = line.split('\t')

	if key==currentkey:

		count += 1
		continue

    	else:

        	if currentkey:
			
			if count not in violations:
				violations[count] = []
			
			violations[count].append(currentkey)
            		
			count = 0
		 
        	currentkey = key
        	count = 1


if currentkey:
	if count not in violations:
		violations[count] = []
        
	violations[count].append(currentkey)

count = 0
flag = 0

od_violations = collections.OrderedDict(sorted(violations.items(), reverse = True))

for k, v in od_violations.iteritems():
	
	for cars in v:
		
		plate_id, state = cars.split(',')
		print '%s, %s\t%d' % (plate_id, state, k)
		count += 1
		
		if count == 20:
			flag = 1
			break

	if flag == 1:
		break
