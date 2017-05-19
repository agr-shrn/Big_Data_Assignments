#!/usr/bin/env python

import csv
import os
import sys


currentkey = None
count = 0

for line in sys.stdin:

    line = line.strip()
    key, value = line.split('\t')

    if key==currentkey:
        count += 1
        continue

    else:

        if currentkey:
            print '%s\t%d' % (currentkey, count)  
            count = 0 

        
        currentkey = key
        count = 1
        

if currentkey:
	print '%s\t%d' % (currentkey, count)

