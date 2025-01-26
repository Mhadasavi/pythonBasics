from pyspark.python.pyspark.shell import spark
from pyspark.sql import SparkSession
from pyspark.sql import Row

from Scraper.CryptoSchema import schema
from Scraper.cryptoTableParser2 import CryptoTableParser2


class CryptoSilverProcessor:

    spark = SparkSession.builder.appName("Cryptos").getOrCreate()
    sc = spark.sparkContext
    table_parser_data = CryptoTableParser2()
    # cleaned_data = [
    #     {
    #         'Name': item.get('Name', 'N/A'),
    #         'Price': item.get('Price', 'N/A'),
    #         '24H Change': item.get('24H Change', 'N/A')
    #     }
    #     for item in table_parser_data.get_crypto_data()
    # ]
    # print(cleaned_data)
    data = [(1, "John Doe", 29), (2, "Jane Smith", 35), (3, "Sam Brown", 22)]
    columns = ["id", "name", "age"]

    # Convert the list of Row objects to a DataFrame
    df = spark.createDataFrame(data, schema=columns)
    # df = spark.createDataFrame(table_parser_data.get_crypto_data())
    # df.printSchema()
    df.show()