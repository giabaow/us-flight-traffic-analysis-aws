from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import lit

# Initialize Glue/Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Input folder containing the 5 Parquet files
input_path = "s3://weather-data-els9cy/weather_parquet/"

# Read all Parquet files in the folder
df = spark.read.parquet(input_path)

# Merge all data into 1 single file
output_path = "s3://weather-data-els9cy/weather_parquet_merged_single/"
df.coalesce(1).write.mode("overwrite").parquet(output_path)

print("All Parquet files merged into a single file successfully!")