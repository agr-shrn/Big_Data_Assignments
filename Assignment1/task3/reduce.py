#!/usr/bin/env python

import csv
import os
import sys


currentkey = None
sum = 0.0
avg = 0.0
count = 0

for line in sys.stdin:

	line = line.strip()
	key, value = line.split('\t')

	if key==currentkey:

		sum += float(value)
        	count += 1
		continue

    	else:

        	if currentkey:
			avg = sum/count
			print '%s\t%.2f, %.2f' % (currentkey, sum, avg)  
            		count = 0
			sum = 0.0
			avg = 0.0
		 

        	currentkey = key
        	sum = float(value)
        	count = 1

if currentkey:
	avg = sum/count
	print '%s\t%.2f, %.2f' % (currentkey, sum, avg)

