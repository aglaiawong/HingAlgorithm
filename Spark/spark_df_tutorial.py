################################
#create df 
################################

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

#create dataframe 
plantDF = sqlContext.read.load('<fileName>')		#create a dataframe

#e.g.
plantDF = sqlContext.read.format('com.databricks.spark.csv').options(delimiter='\t', header='true', inferschema='true').load("/databricks-datasets/power-plant/data")

#check datatypes
plantDF.dtypes		#return: [('AT', 'double'), ('V', 'double')...]

#show the table in html 
display(plantDF)

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
	
altPlantDF = sqlContext.read.format('com.databricks.spark.csv').options(delimiter='\t', header='true').load("/databricks-datasets/power-plant/data", schema=customSchema)	#use schema instead of inferring one 

############################################
# query the dataframe: drop and add table  #
############################################

#sqlContext ~ a mini db, queries issued with '.sql'
sqlContext.sql("DROP TABLE IF EXISTS plant_dataset")
dbutils.fs.rm("dbfs:/user/hive/warehouse/plant_dataset", True)

#alternatively, sql executed in this way 
%sql
SELECT * FROM plant_dataset
des plant_dataset	#describe schema: (colName, dType)

# dataframe needed to be converted into table before query 
sqlContext.registerDataFrameAsTable(plantDF, "plant_dataset")

# convert table back into dataframe: i.e. deregister 
df = sqlContext.table("plant_dataset")
display(df.describe())		#get stat abt data: count, mean, stddev, min, max 


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


#splitting performed on df
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
lr.setPredictionCol("Prediction_PE")\
  .setLabelCol("PE")\
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

#bookmark here:
featuresNoLabel = [col for col in datasetDF.columns if col != "PE"]



























