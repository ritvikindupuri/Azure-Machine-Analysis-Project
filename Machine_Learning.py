# the Spark MLlib library (pyspark.ml) was used to perform Data Analysis. This involves two steps:

#Vector Assembler: Combining all feature columns into a single "vector" column.

# KMeans: Training the model on that vector column.


from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans

# 1. Combine features into a single vector column
assembler = VectorAssembler(
    inputCols=['error1', 'error2', 'error3', 'error4', 'error5'], 
    outputCol="features"
)
vec_df = assembler.transform(machine_features)

# 2. Train K-Means Model
kmeans = KMeans(k=3, seed=1)
model = kmeans.fit(vec_df)

# 3. Predict Clusters
predictions = model.transform(vec_df)
predictions.select("machineID", "prediction").show(5)
