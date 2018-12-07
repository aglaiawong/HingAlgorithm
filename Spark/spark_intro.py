# load the data
wordsList = ['cat', 'elephant', 'rat', 'rat', 'cat']

#divide into RDD partions, here, 4 partions 
wordsRDD = sc.parallelize(wordList, numSlices=4)
# c.f. when data read from file 
import os.path
filePath = 'dbfs:/FileStore/tables/shakespere.txt'
spRDD = sc.textFile(filePath, 8).map(removePunctuation)

#apply function via map: take each elements in partions and perform operations 
capitalRDD = wordsRDD.map(capitalize)		#map(x) = for each element in each rdd, do...x
# identical 
capitalRDD = wordsRDD.map(lambda x: capitalize(x))

#label each word with count 
wordPairs = wordsRDD.map(lambda x: (x,1))


##################
#Get word counts : a key-centered aggregation approach 
# step 1: group elements of same key tgt, so a key get a list of values corresponding to items
# step 2: aggregate, sum up all value for particular key 
##################

# M1: groupByKey() + map()
# groupByKey() group values under same key into a single sequence 
wordsGrouped = wordPairs.groupByKey()
# However, the above just returns you: 
# rat: [1, 1] elephant: [1] cat: [1, 1]
# Do the following to get: rat:[2], elements:[1]

# here, x[1] is a list of values for particular key 
wordCountsGrouped = wordsGrouped.map(lambda x: (x[0], sum(x[1]))		#sum() on an list gives the total counts 

# M2: count by reduceByKey()
wordCountsGrouped = wordPairs.reduceByKey(lambda a,b: a+b)

# a simple word count program looks like one-line 
wordCountsCollected = wordsRDD.map(lambda x: (x,1)).reduceByKey(lambda a,b: a+b).collect()

# metadata: get number of records within the RDD
uniqueWords = wordCounts.count()

# count total number of words in document
# before counting, must use flatMap()
spWordsRDD = spRDD.flatMap(lambda x:x.split())	#return a list on each elements in rdd; thus, flattened to give a single array 
spWordsCount = spWordsRDD.count()

spWordsRDD.top(5)	#return elements in descending order 

# user-define transfomation: take a RDD as input, output a rDD
def wordCount(wordlistRDD):
	wordPairs_t = wordListRDD.map(lambda x: (x,1)).reduceByKey(lambda a,b:a+b)
	return wordPairs_t

# takeOrdered is ascending 
top10WordsAndCounts = wordCount(spWordsRDD).takeOrdered(10, lambda x:-x[1])
# get results as a list 
top10WordsAndCounts.collect()

# c.f. 
top10WordsAndCounts.cache()




