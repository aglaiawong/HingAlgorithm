################################
#create df 
################################

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

#create dataframe from data src
plantDF = sqlContext.read.load('<fileName>')		#create a dataframe

#create df from existing RDD of Row object
lines = sc.textFile(".../people.txt")	#lines of text splitted by '\n'
parts = lines.map(lambda l: l.split(','))

# form a RDD of row object by map(); key as column name and schema inferred 
# a data frame only formed from a collection of Row() objects in RDD
people = parts.map(lambda p: Row(name=p[0], age=int(p[1])))

# infer schema, create table from RDD of Row objects
schemaPeople = spark.createDataFrame(people)
# then register the view, i.e. a Hive table in memory; require caching
schemaPeople.createOrReplaceTempView("people")
# use sql to inquire a table 
teenagers = spark.sql("Select name FROM people WHERE age>=18")
# rdd convert table into RDD of Row objects
teenNames = teenagers.rdd.map(lambda p: "Name: " + p.name).collect()


#create dataframe from csv 
df = spark.read.csv('/mnt/sf_open_data/.../file.csv', header=True, schema=fireSchema)

#e.g.
plantDF = sqlContext.read.format('com.databricks.spark.csv').options(delimiter='\t', header='true', inferschema='true').load("/databricks-datasets/power-plant/data")


###########################
# explore the data 
###########################
#check datatypes
plantDF.dtypes		#return: [('AT', 'double'), ('V', 'double')...]
df.printSchema()

#show the table in html 
display(plantDF)
plantDF.show()	#an plain text table with records 

#show table with limited records
display(df.limit(5))

#get a list of column names of df 
df.columns

#get total number of records 
df.count()


###########################
# user defined schema
###########################
from pyspark.sql.types import *

# Custom Schema for Power Plant
# a StructType object 
customSchema = StructType([ \
    StructField("AT", DoubleType(), True), \
    StructField("V", DoubleType(), True), \
    StructField("AP", DoubleType(), True), \
    StructField("RH", DoubleType(), True), \
    StructField("PE", DoubleType(), True)])

#create dataframe by sparkContext.read.load()
altPlantDF = sqlContext.read.format('com.databricks.spark.csv').options(delimiter='\t', header='true').load("/databricks-datasets/power-plant/data", schema=customSchema)	#use schema instead of inferring one 

############################################
# query the dataframe: drop and add table  #
############################################

#sqlContext ~ distributed SQL Enginer: ~sqlContext as a mini db, queries issued with '.sql()'
from pyspark.sql import SQLContext
sqlContext.sql("DROP TABLE IF EXISTS plant_dataset")
dbutils.fs.rm("dbfs:/user/hive/warehouse/plant_dataset", True)

# dataframe needed to be converted into table before query 
sqlContext.registerDataFrameAsTable(plantDF, "plant_dataset")
# Conversely, convert table back into dataframe: i.e. deregister 
df = sqlContext.table("plant_dataset")

#M1: sql queries
%sql
SELECT * FROM plant_dataset
des plant_dataset	#describe schema of a table: (colName, dType)
#M2: sql queries
sqlContext.sql("DROP TABLE IF EXISTS plant_dataset")

# convert table back into dataframe: i.e. deregister 
df = sqlContext.table("plant_dataset")
display(df.describe())		#get stat abt data: count, mean, stddev, min, max 

# sql dataframe: select columns 
df.select("name").show()
df.select(df['name'], df['age']+1).show()
df.filter(df['age']>21).show()
df.groupBy("age").count().show()	#count usually follows groupBy

#########################
# feature construction  #
#########################

#feature construction
from pyspark.ml.feature import VectorAssembler
#Get the DF to allow colum-wise operation 
datasetDF = sqlContext.table("plant_dataset")	
vectorizer = VectorAssembler()
vectorizer.setInputCols(["AT", "V", "AP", "RH"])	#combine several columns tgt to form a feature vector 
vectorizer.setOutputCol("features")		# name of output column


#splitting performed on df; split on df, not on table! 
(split15DF, split85DF) = datasetDF.randomSplit([0.15, 0.85], seed=1900009193L)
#cache the splitted datasets 
testSetDF = split85DF.cache()
trainSetDF = split15DF.cache()

###########################
# model building in spark #
###########################
from pyspark.ml.regression import LinearRegression
from pyspark.ml.regression import LinearRegressionModel
from pyspark.ml import Pipeline

# model constructor 
lr = LinearRegression()

# understand model parameters 
lr.explainParams()		#individually call fnc on each param to set, like the following
lr.setPredictionCol("Prediction_PE")\	#rename the prediction col 
  .setLabelCol("PE")\		#col in df
  .setMaxIter(100)\
  .setRegParam(0.15)

###########################
# create a pipeline
# - pipeline contains a series of stages in sequential execution 
# - each stage either an estimator or a transformer 
# - pipeline.fit() may equal to one of the following:
#	* estimator.fit()
#	* transformer.transform()
# - the fitted model = pipelineModel 
###########################

lrPipeline = Pipeline()
lrPipeline.setStages([vectorizer, lr])		#2 stages in sequence: feature vector, 
lrModel = lrPipeline.fit(trainSetDF)		#return: pipelineModel

# get results from pipelineModel: must specify the stage, see below 
intercept = lrModel.stages[1].intercept		#recall lrModel is a pipelineModel, only the 2nd stage is the model fitting procedure, which gives intercept and coefficients 
weights = lrModel.stages[1].coefficients

#only keep feature columns, i.e. exclude prediction col 
featuresNoLabel = [col for col in datasetDF.columns if col != "PE"]

#merge weights and labels
coefficients = zip(weights, featureNoLabel)
#sort the coefficient from greatest absolute weight 
coefficient.sort(key=lambda tup: abs(tup[0]), reverse=True)

######################
# print linear model #
######################
equation = "y = {intercept}".format(intercept=intercept)
variables = []
for x in coefficents:
    weight = abs(x[0])
    name = x[1]
    symbol = "+" if (x[0] > 0) else "-"
    equation += (" {} ({} * {})".format(symbol, weight, name))
print("Linear Regression Equation: " + equation)


##########################
# prediction using model #
##########################

# predict on test set 
resultsDF = lrModel.transform(testSetDF).select("AT", "V", "AP", "RH", "PE", "Prediction_PE")
#model.transform() fills the predictionCol set in model with the prediction 

from pyspark.ml.evaluation import RegressionEvaluator
#to evaluate, you need to set which col is the prediction, which is original col 
regEval = RegressionEvaluator(predictionCol="Prediction_PE", labelCol="PE", metricName="rmse")
rmse = regEval.evaluate(resultsDF)
#change evaluation metric
r2 = regEval.evaluate(resultsDF, {regEval.metricName: "r2"})


####################
# Cross validation 
# i) install list of parameters for tunning in to the model 
# ii) build a paramGrid from it 
# iii) install paramGrid into cross-validator
####################
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

#constructor for cross-validator
crossval = CrossValidator(estimator=lrPipeline, evaluator=regEval, numFolds=3)
regParam = [x / 200.0 for x in range(1,11)]
# i) install regParam into the model; 		ii) construct a paramGrid from the modified model 
paramGrid = (ParamGridBuilder().addGrid(lr.regParam, regParam).build())
crossval.setEstimatorParamMaps(paramGrid)
#get model as a result of cv
#cv performed on TS, not test set 
cvModel = crossval.fit(trainingSetDF).bestModel


# Add the .distinct() transformation to keep only distinct rows
# The False below expands the ASCII column width to fit the full text in the output
fireServiceCallsDF.select('CallType').distinct().show(35, False)

#How many incidents of each call type were there?
display(df.select('callType').groupBy('CallType').count().orderBy("count", ascending=False)

#bkmk: Spark Logo Tiny Doing Date/Time Analysis

###################
# add & delete columns 
###################
from_pattern1 = 'MM/dd/yyyy'
to_pattern1 = 'yyyy-MM-dd'

from_pattern2 = 'MM/dd/yyyy hh:mm:ss aa'
to_pattern2 = 'MM/dd/yyyy hh:mm:ss aa'


fireServiceCallsTsDF = fireServiceCallsDF \
  .withColumn('CallDateTS', unix_timestamp(fireServiceCallsDF['CallDate'], from_pattern1).cast("timestamp")) \
  .drop('CallDate')

fireServiceCallsDF.printSchema()

df.select('CallDateTS').distinct().orderBy()

# take a particular column and show first 5 records 
df.select('CallType').show(5, False)   # truncation of super-long record == False 

# how many incidents of each call type there? 
# the name is arbitrary for orderBy() col
display(df.select('CallType').groupBy('CallType').count().orderBy("count", ascending=False))


%sql SELECT count(*) FROM fireServiceVIEW;

#Which neighborhood in SF generated the most calls last year?
%sql SELECT `NeighborhoodDistrict`, count(`NeighborhoodDistrict`) AS Neighborhood_Count FROM fireServiceVIEW WHERE year(`CallDateTS`) == '2015' GROUP BY `NeighborhoodDistrict` ORDER BY Neighborhood_Count DESC LIMIT 15;

joinedDF = fireServiceDF.join(incidentsDF, fireServiceDF.IncidentNumber == incidentsDF.IncidentNumber)

#from spark df to pandas df 
pandas2016 = joinedDF(year('CallDateTS')=='2016').toPandas()

display(joinedDF.filter(year('CallDateTS') == '2015').filter(col('NeighborhoodDistrict') == 'Russian Hill').groupBy('Primary Situation').count().orderBy(desc("count")).limit(10))
#Selects column based on the column name and returns it as a Column. 

df.count()		#get total number of records 

# col():Selects column based on the column name and returns it as a Column. 
joinedDF.filter(year('CallDateTS') == '2015').filter(col('NeighborhoodDistrict') == 'Tenderloin').count().orderBy(desc("count")).limit(10))

joinedDF.filter(year('CallDateTS')=='2015').filter(col('NeighborhoodDistrict')=='Tenderloin').groupBy('Primary Situation').count().orderBy(des("count")).limit(10))
# after groupBy(), must followed by aggregative count(), then only 2 columns returned: primary_situ & count 
# after count, column automatically named as 'count()'

#filter(Column condition)
#Filters rows using the given condition. This explains why filter(col(colName))

#groupBy(): Groups the Dataset using the specified columns, so that we can run aggregation on them. 
#this explains why only specified column returned after groupBy()

################################################
# Spark dataset reference: https://spark.apache.org/docs/2.3.0/api/java/index.html?org/apache/spark/sql/Dataset.html
################################################

pddf = df.toPandas()















