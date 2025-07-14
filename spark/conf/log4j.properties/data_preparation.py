from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


spark = SparkSession.builder \
        .appName("RetailExploration") \
        .master("spark://spark-master:7077") \
        .getOrCreate()

## Read the data from HDFS
df = spark.read.csv.load("hdfs://namenode:8020/data/raw/Online_Retail.csv", header=True, inferSchema=True)



