#change each element in RDD without creating any pairs
#similar to map(), except foreach() make changes in-place in RDD
sc.parallelize([1,2,3,4,5],10).foreach(lambda x : x-1)

# any iterables/collections in user program can be parallelized as following
conf = SparkConf().setAppName(appName).setMaster(master)
data=[1,2,3,4,5]		# variable defined in user program 
distData = sc.parallelize(data, 10)		#turn into spark context for parallelization 

#####################
#Submit spark application to cluster (reference only)
#####################

# Run a Python application on a Spark standalone cluster
./bin/spark-submit \
  --master spark://207.184.161.138:7077 \
  examples/src/main/python/pi.py \
  1000
 
# Run application locally on 8 cores
./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master local[8] \
  /path/to/examples.jar \
  100
  
# Run on a YARN cluster
export HADOOP_CONF_DIR=XXX
./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master yarn \
  --deploy-mode cluster \  # can be client for client mode
  --executor-memory 20G \
  --num-executors 50 \
  /path/to/examples.jar \
  1000

#######################
# CLOSURE
####################### 

#SNIPPET 1
counter = 0		#global in DRIVER: not visible to executors 
rdd = sc.parallelize(data)

# Wrong: Don't do this!!
def increment_counter(x):
    global counter
    counter += x

#called by each executor, with their own copy of increment_counter() and counter variable	
#thus, not updated
rdd.foreach(increment_counter)
print("Counter value: ", counter)

#remedy:
accum = sc.accumulator(0)
sc.parallelize([1,2,3,4]).foreach(lambda x: accum.add(x))		#foreach() is an action: as it returns a list of results 

#broadcast variables 
broadcastVar = sc.broadcast([1, 2, 3])
broadcastVar.value

#another example 
accum = sc.accumulator(0)
def g(x):
    accum.add(x)		#python add(): 2 args 
    return f(x)
data.map(g)
# Here, accum is still 0 because no actions have caused the `map` to be computed.

# LOCALLY printing each elements in RDD; i.e. not aggregated at driver prog side 
rdd.foreach(print)		#an action, return a list of results. 
rdd.map(print)

# print elements in RDD across executors in driver 
# after actions like take(), collect() --> cannot apply map(), which only for rdd distributed across machines only. 
rdd.collect().foreach(print)
# or, just print a few of them
rdd.take(100).foreach(print)



