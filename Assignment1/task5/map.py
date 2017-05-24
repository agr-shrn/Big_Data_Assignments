#!/usr/bin/env python

import csv
import os
import sys


for line in sys.stdin:

	entry = csv.reader([line])

	for row in entry:    			
		
		print '%s,%s\t1' % (row[14],row[16])                  
