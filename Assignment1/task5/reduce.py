#!/usr/bin/env python

import csv
import os
import sys


currentkey = None
count = 0
max = 0

for line in sys.stdin:

	line = line.strip()
	key, value = line.split('\t')

	if key==currentkey:

		count += 1
		continue

    	else:

        	if currentkey:
			
			if count > max:
				max = count
				plate_id, state = currentkey.split(',')

            		count = 0
		 
        	currentkey = key
        	count = 1


if currentkey:
	if count > max:
		max = count
		plate_id, state = currentkey.split(',')


print '%s, %s\t%d' % (plate_id, state, max)
