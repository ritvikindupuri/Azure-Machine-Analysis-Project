# Create a matrix: Rows = Machines, Columns = Error Counts
machine_features = df.groupBy("machineID") \
    .pivot("errorID") \
    .count() \
    .na.fill(0)

machine_features.show(5)
