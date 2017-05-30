#!/usr/bin/env python

import csv
import os
import sys


currentkey = None
weekends = ["05", "06", "12", "13", "19", "20", "26", "27"]
count_weekday = 0.0
count_weekend = 0.0
avg_weekend = 0.0
avg_weekday = 0.0

for line in sys.stdin:

	line = line.strip()
	key, value = line.split('\t')

	if key==currentkey:
		
		if value in weekends:
			count_weekend += 1
		
		else:
			count_weekday += 1
		
		continue

    	else:

        	if currentkey:
			
			avg_weekend = count_weekend/8.0
			avg_weekday = count_weekday/23.0

			print '%s\t%.2f, %.2f' % (currentkey, avg_weekend, avg_weekday)  
            		
			count_weekend = 0.0
			count_weekday = 0.0
			avg_weekend = 0.0
			avg_weekday = 0.0
		 
        	
		currentkey = key
        	
		if value in weekends:
			count_weekend = 1.0
		else:
			count_weekday = 1.0


if currentkey:
	
	avg_weekend = count_weekend/8.0
	avg_weekday = count_weekday/23.0

        print '%s\t%.2f, %.2f' % (currentkey, avg_weekend, avg_weekday)
