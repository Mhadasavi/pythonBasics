from pyspark.sql.types import StringType, StructField, StructType

schema = StructType([
    StructField('Name', StringType(), True),
    StructField('Price', StringType(), True),
    StructField('24H Change', StringType(), True)
])