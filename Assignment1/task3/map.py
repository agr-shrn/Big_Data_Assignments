#!/usr/bin/env python

import csv
import os
import sys


for line in sys.stdin:

    entry = csv.reader([line])

    for row in entry:
    	print '%s\t%s' % (row[2],row[12])

                    
