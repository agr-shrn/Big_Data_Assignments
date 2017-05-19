#!/usr/bin/env python

import csv
import os
import sys

# row = []
# csv_line = []

for line in sys.stdin:

    entry = csv.reader([line])

    for row in entry:
        if len(row) > 18:
            print '%s\t%s,%s,%s,%s' % (row[0], row[14], row[6], row[2], row[1])

        else:
            print '%s\t%s' % (row[0], row[1])            