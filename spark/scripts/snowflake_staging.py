from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField,
    StringType, IntegerType, DoubleType
)

spark = SparkSession.builder \
    .appName("Retail_Snowflake_Staging") \
    .master("spark://retail-spark-master:7077") \
    .getOrCreate()

schema = StructType([
    StructField("invoice_no",   StringType(),  True),
    StructField("stock_code",   StringType(),  True),
    StructField("description", StringType(),  True),
    StructField("quantity",    IntegerType(), True),
    StructField("invoice_date", StringType(),  True),
    StructField("unit_price",   DoubleType(),  True),
    StructField("customer_id",  StringType(),  True),
    StructField("country",     StringType(),  True),
    StructField("revenue",     DoubleType(),  True),
    StructField("is_return",   IntegerType(),  True)
])


df = spark.read.csv("hdfs://namenode:8020/data/silver/retail_cleaned.csv", header=True, schema=schema)

df.write \
  .format("snowflake") \
  .option("sfURL", "TRLIYPI-XK63730.snowflakecomputing.com") \
  .option("sfUser", "KINGOOZ") \
  .option("sfPassword", "055Hkhiahl@.com") \
  .option("sfDatabase", "RETAIL_SALES") \
  .option("sfSchema", "STAGING") \
  .option("sfWarehouse", "COMPUTE_WH") \
  .option("dbtable", "SILVER_DATA") \
  .option("sfRole", "ACCOUNTADMIN") \
  .mode("overwrite") \
  .save()
