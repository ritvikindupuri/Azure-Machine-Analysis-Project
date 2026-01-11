from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

spark = SparkSession.builder.appName("PdM_Analysis").getOrCreate()

# Load CSV into Spark DataFrame
df = spark.read.csv("PdM_errors.csv", header=True, inferSchema=True)
df = df.withColumn("datetime", to_timestamp(col("datetime")))
