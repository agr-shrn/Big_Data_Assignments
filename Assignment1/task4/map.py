#!/usr/bin/env python

import csv
import os
import sys


for line in sys.stdin:

    entry = csv.reader([line])

    for row in entry:
    	
	if row[16] == "NY":
    		
		print "NY\t1"
	
	else:
		print "Other\t1"                   
