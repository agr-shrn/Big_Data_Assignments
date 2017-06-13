from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader 


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: task1 <file> <file>", file=sys.stderr)
        exit(-1)

    def new_map(x):
        if len(x) > 18: 
            return(str(x[0]) , str(x[14]) + "," + str(x[6])+ "," + str(x[2])+ "," + str(x[1]))
        else:
            return(str(x[0]), "A")

    sc = SparkContext()
    lines_park = sc.textFile(sys.argv[1], 1) 
    lines_park2 = lines_park.mapPartitions(lambda x: reader(x))

    lines_open = sc.textFile(sys.argv[2], 1) 
    lines_open2 = lines_open.mapPartitions(lambda x: reader(x))

    lines_comb = lines_open2 + lines_park2

    lines_final = lines_comb.map(lambda x: new_map(x)).groupByKey().collect()

    final = []

    for line in lines_final:
        if len(line[1]) == 1:
            for element in line[1]:
                if len(element) > 1: 
                    final.append(line[0] + "\t" + element)

    counts = sc.parallelize(final);
    counts.saveAsTextFile("task1.out")

    sc.stop()


