from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.evaluation import RegressionEvaluator

# start Spark
spark = SparkSession.builder.appName('Predict_Temp').enableHiveSupport().getOrCreate()

# import the Hive table into Spark
home_data = spark.read.table('home_temps')

# define which columns are features and which one is the target.
feature_columns = ['dining_temp',
                   'dining_hum',
                   'bedroom_temp',
                   'bedroom_hum',
                   'bathroom_temp',
                   'bathroom_hum'
                   ]
target_column = 'outdoor_temp'

# split into training and test data.
train_df, test_df = home_data.randomSplit([0.8,0.2], seed = 19)

# Define the pipeline stages
vector_assembler = VectorAssembler(inputCols = feature_columns,
                                   outputCol = "raw_features")
# Because the humidity and temperatures are on different scales we use standard scaler on all the data.
scaler = StandardScaler(inputCol = "raw_features",
                        outputCol = "scaled_features",
                        withStd = True,
                        withMean = True)
regression = LinearRegression(featuresCol = "scaled_features",
                              labelCol = target_column)

# define the pipeline
pipeline = Pipeline(stages = [vector_assembler, scaler, regression])

# fit the pipeline
pipeline_model = pipeline.fit(train_df)
# test the model
predictions = pipeline_model.transform(test_df)



# calculate evaluation metrics for the model
rmse_evaluator = RegressionEvaluator(labelCol = target_column, predictionCol = 'prediction', metricName = 'rmse')
r2_evaluator = RegressionEvaluator(labelCol = target_column, predictionCol = 'prediction', metricName = 'r2')


rmse_value = rmse_evaluator.evaluate(predictions)
r2_value = r2_evaluator.evaluate(predictions)

import happybase

# Connect to HBase using Happybase
connection = happybase.Connection('hbase-thrift-host')
table = connection.table('Models')

table.put(b'1',{
    'model_type:model_type': 'linear_regression',
    'metrics:accuracy': str(rmse_value),
    'metrics:f1_score': str(r2_value)
})

print("Metrics written to HBase.")

spark.stop()