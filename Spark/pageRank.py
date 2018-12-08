from operator import *
import re

def computeContribs(urls, rank):	#calculate contributions to a target website by each of its neighbours
	num_urls = len(urls)
	for url in urls:
		yield (url, rank/num_urls)

def parseNeighbors(urls):
	parts = re.split(r'\s+', urls)		#split by space
	return parts[0], parts[1]	#return as a tuple 

lines = sc.textFile('url.txt')
links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()		#avoid same url pointing to itself: Baidu	Baidu
#after map(), return a RDD. Call distinct() on this RDD eliminates two (Baidu, Baidu)
#after groupByKey(), return an RDD of: (Baidu, [Weibo, Android, Yahoo, Google]), i.e. Google points to Baidu

#initialize mass for each page being pointed at 
ranks = links.map(lambda (url, neighbours): (url, 1.0))		#use a tuple in lambda 

for iteration in xrange(10):
	contribs = links.join(ranks).flatMap(lambda (url, (urls, rank)): computeContribs(urls, rank))
	#after join(): (url, [neighbour]) + (url, rank) = (url, ([neighbour], rank))
	#self comes first in value pair; thus, WRONG: (url, (rank, neighbour))
	
	ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85+0.15)		#Pass each value in the key-value pair RDD through a map function without changing the keys; this also retains the original RDD’s partitioning. 
	# mapValues(): for further operatios on values only

for(link, rank) in ranks.collect():
	print "%s has rank: %s." % (link, rank)

	
from operator import *
import re

def computeContribs(urls, rank):
	num_urls = len(urls)
	for url in urls:
		yield (url, rank/num_urls)

def parseNeighbors(urls):
	parts = re.split(r'\s+', urls)		#split by space
	return parts[0], parts[1]

lines = sc.textFile("dbfs:/FileStore/tables/url2.txt")
links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()		#avoid same url pointing to itself: Baidu	Baidu

def printRDD(r):
	print r


ranks = links.map(lambda (url, neighbours): (url, 1.0))
for iteration in xrange(10):
	# LHS url distributes its PR mass to each of its neighbours 
    contribs = links.join(ranks).flatMap(lambda (url, (urls, rank)): computeContribs(urls, rank))   #rank is for LHS's link, i.e. pointing out to neighbour links
	
	print(contribs.take(5))
	
    # each neighbor collect its incoming PR
	ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85+0.15)
    
	print('--------------------------------')
	print(ranks.take(5))

#for (link, rank) in ranks.collect():
#	print "%s has rank: %s." % (link, rank)

ranks.take(4)
	
	
	
'''
from __future__ import print_function

import re
import sys
from operator import add

from pyspark.sql import SparkSession


def computeContribs(urls, rank):
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


def parseNeighbors(urls):
    parts = re.split(r'\s+', urls)
    return parts[0], parts[1]


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: pagerank <file> <iterations>", file=sys.stderr)
        exit(-1)

    print("""WARN: This is a naive implementation of PageRank and is
          given as an example! Please refer to PageRank implementation provided by graphx""",
          file=sys.stderr)

    
    spark = SparkSession\
        .builder\
        .appName("PythonPageRank")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])

    links = lines.map(lambda urls: parseNeighbors(urls)).distinct().groupByKey().cache()

    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    for iteration in range(int(sys.argv[2])):
        
        contribs = links.join(ranks).flatMap(
            lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))

        
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

    
    for (link, rank) in ranks.collect():
        print("%s has rank: %s." % (link, rank))

spark.stop()
'''