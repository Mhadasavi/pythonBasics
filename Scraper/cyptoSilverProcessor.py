from pyspark.python.pyspark.shell import spark
from pyspark.sql import SparkSession, Window
from pyspark.sql import Row
from pyspark.sql import functions as F

from Scraper.CryptoSchema import schema
from Scraper.CryptoUtils import get_usd_to_inr
from Scraper.cryptoTableParser import CryptoTableParser


class CryptoSilverProcessor:

    spark = SparkSession.builder.appName("Cryptos").getOrCreate()
    sc = spark.sparkContext

    table_parser_data = CryptoTableParser()

    # Convert the list of Row objects to a DataFrame
    df = spark.createDataFrame(table_parser_data.get_crypto_data(), schema=schema)

    # Transformation includes removing $ and , from Price column and converting it to float
    custom_df = df.withColumn("Trimmed Price", F.regexp_replace(F.col("Price"), '[$,]', '').cast("float") )

    # get exchange rate
    trimmed_exchange_rate = get_usd_to_inr()
    print(f'trimmed_exchange_rate : {trimmed_exchange_rate}')

    # Assign autoincrementing Id column
    window = Window.orderBy(F.lit(1))
    custom_df = custom_df.withColumn("Id" , F.row_number().over(window))

    # Populate Price in INR column
    custom_df = custom_df.withColumn("Price in INR", F.col("Trimmed Price").cast("float") * trimmed_exchange_rate).drop("Trimmed Price")
    custom_df = custom_df.withColumn("Price in INR", F.round(F.col("Price in INR"), 2))
    custom_df.show()

    # User Input to export to csv
    user_input = input("do you want to export to csv (yes/no)..." )
    list_of_valid_inputs = ['yes', 'y']
    export_csv = user_input.lower() in list_of_valid_inputs

    # export to csv
    if export_csv:
        custom_df.coalesce(1).write.mode("overwrite").option("header", "true").csv("data/crypto_silver.csv")
