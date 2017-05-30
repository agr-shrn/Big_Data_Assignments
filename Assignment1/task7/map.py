#!/usr/bin/env python

import csv
import os
import sys


for line in sys.stdin:

    entry = csv.reader([line])

    for row in entry:
        row[1].strip()
        year, month, day = row[1].split('-')
        print '%s\t%s' % (row[2], day)
