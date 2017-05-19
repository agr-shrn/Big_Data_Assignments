#!/usr/bin/env python

import csv
import os
import sys


currentkey = None
count = 0
values = []

for line in sys.stdin:

	line = line.strip()
	key, value = line.split('\t')

    	if key==currentkey:
        	count = 0
        	continue

    	else:

		if currentkey and count == 1 and len(values) == 4:
			print '%s\t%s, %s, %s, %s' % (currentkey, values[0], values[1], values[2], values[3])
	
		elif currentkey and count == 1 and len(values) == 5:
			print '%s\t%s, %s, %s, %s' % (currentkey, values[0] + "," + values[1], values[2], values[3], values[4])
	
		count = 0 

        
        currentkey = key
        entry = csv.reader([value])

        for row in entry:
            if len(row) > 1:
                count = 1
                values = row

  
if currentkey and count == 1 and len(values) == 4:
	print '%s\t%s, %s, %s, %s' % (currentkey, values[0], values[1], values[2], values[3])

elif currentkey and count == 1 and len(values) == 5:
	print '%s\t%s, %s, %s, %s' % (currentkey, values[0] + "," + values[1], values[2], values[3], values[4])
