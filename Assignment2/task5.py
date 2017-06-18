from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: task5 <file>", file=sys.stderr)
        exit(-1)

    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1) 
    lines2 = lines.mapPartitions(lambda x: reader(x))

    counts = lines2.map(lambda x: (str(x[14]) + ", " + str(x[16]), 1)).reduceByKey(add)

    counts_sorted = counts.sortBy(lambda x: x[1], false)
    
    final = sc.parallelize(counts_sorted.take(1))
    final2 = final.map(lambda x: '%s\t%d' % (x[0], x[1]))

    final2.saveAsTextFile("task5.out")

    sc.stop()




