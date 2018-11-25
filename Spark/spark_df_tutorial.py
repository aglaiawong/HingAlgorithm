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

#create dataframe by sparkContext.read.load()
altPlantDF = sqlContext.read.format('com.databricks.spark.csv').options(delimiter='\t', header='true').load("/databricks-datasets/power-plant/data", schema=customSchema)	#use schema instead of inferring one 

############################################
# query the dataframe: drop and add table  #
############################################

#sqlContext ~ sqlContext as a mini db, queries issued with '.sql()'
sqlContext.sql("DROP TABLE IF EXISTS plant_dataset")
dbutils.fs.rm("dbfs:/user/hive/warehouse/plant_dataset", True)

# dataframe needed to be converted into table before query 
sqlContext.registerDataFrameAsTable(plantDF, "plant_dataset")
# Conversely, convert table back into dataframe: i.e. deregister 
df = sqlContext.table("plant_dataset")

#M1: sql queries
%sql
SELECT * FROM plant_dataset
des plant_dataset	#describe schema: (colName, dType)
#M2: sql queries
sqlContext.sql("DROP TABLE IF EXISTS plant_dataset")

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
#model.transform() transform model by appending a col of prediction to the dataset being tested. 

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



























