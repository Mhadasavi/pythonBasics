from pyspark.sql.types import StringType, StructField, StructType

schema = StructType([
    StructField('Id', StringType(), True),
    StructField('Name', StringType(), True),
    StructField('Price', StringType(), True),
    StructField('24H Change', StringType(), True),
    StructField('Price in INR', StringType(), True)
])