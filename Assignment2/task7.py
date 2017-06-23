from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader 


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: task7 <file>", file=sys.stderr)
        exit(-1)

    def new_map(x):
        if x[1][0] in weekends: 
            return(x[0], [1, 0])
        else:
            return(x[0], [0, 1])

    weekends = ["05", "06", "12", "13", "19", "20", "26", "27"]

    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1) 
    lines2 = lines.mapPartitions(lambda x: reader(x))

    date_count = lines2.map(lambda x: (x[2].encode('utf-8'), [str(x[1])[-2:], 1, 1])).map(lambda x: new_map(x))

    sums = date_count.reduceByKey(lambda x,y:[x[0] + y[0], x[1] + y[1]])

    final = sums.map(lambda x: '%s\t%.2f, %.2f' % (x[0], float(x[1][0])/8, float(x[1][1])/23))


    final.saveAsTextFile("task7.out")

    sc.stop()


