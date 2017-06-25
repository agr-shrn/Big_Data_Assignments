from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: task5 <file>", file=sys.stderr)
        exit(-1)

    def new_map(x):
        if x[0] == "NY": 
            return(x[0], 1)
        else:
            return("Other", 1)


    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1) 
    lines2 = lines.mapPartitions(lambda x: reader(x))

    state_count = lines2.map(lambda x: (x[16].encode('utf-8'), 1)).map(lambda x: new_map(x))

    sums = state_count.reduceByKey(lambda x,y:x+y)

    final = sums.map(lambda x: '%s\t%d' % (x[0], x[1]))

    final.saveAsTextFile("task4.out")

    sc.stop()




