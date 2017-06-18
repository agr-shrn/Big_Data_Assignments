from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader 


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: task3 <file>", file=sys.stderr)
        exit(-1)

    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1) 
    lines2 = lines.mapPartitions(lambda x: reader(x))

    amounts = lines2.map(lambda x: (x[2].encode('utf-8'), [x[12], 1]))

    sums = amounts.reduceByKey(lambda x,y:[x[0] + y[0], x[1] + y[1]])

    final = sums.map(lambda x: '%s\t%.2f, %.2f' (x[0], x[1][0], x[1][0]/x[1][1]))


    final.saveAsTextFile("task3.out")

    sc.stop()


