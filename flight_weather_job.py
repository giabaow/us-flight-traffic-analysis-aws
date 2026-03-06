#flight_weather_job
import sys
import boto3
import os
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import col, lit

# Initialize Glue/Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

s3 = boto3.client('s3')

# Input JSON folder
input_path = "s3://weather-data-els9cy/weather/*.json"

# Temporary output folder
temp_output = "s3://weather-data-els9cy/temp_weather_parquet/"

# Final output file
final_output_bucket = "weather-data-els9cy"
final_output_key = "weather_parquet/weather_merged.parquet"

# Read JSON
weather_df = spark.read.option("multiline", "true").json(input_path)

# Flatten and cast numeric fields
flat_df = weather_df.select(
    col("year").cast("int"),
    col("month").cast("int"),
    col("coord.lat").cast("double").alias("lat"),
    col("coord.lon").cast("double").alias("lon"),
    col("main.temp").cast("double").alias("temp"),
    col("main.humidity").cast("double").alias("humidity"),
    col("weather")[0]["main"].alias("weather_main"),
    col("weather")[0]["description"].alias("weather_description"),
    col("wind.speed").cast("double").alias("wind_speed"),
    col("wind.deg").cast("double").alias("wind_deg"),
    col("dt").cast("bigint").alias("timestamp")
)

# Write to temporary folder as a single file
flat_df.coalesce(1).write.mode("overwrite").parquet(temp_output)

# Find the generated part-file and rename it
bucket_name = final_output_bucket
temp_prefix = "temp_weather_parquet/"
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=temp_prefix)
for obj in response.get('Contents', []):
    key = obj['Key']
    if key.endswith(".parquet"):
        copy_source = {'Bucket': bucket_name, 'Key': key}
        s3.copy_object(Bucket=bucket_name, CopySource=copy_source, Key=final_output_key)
        s3.delete_object(Bucket=bucket_name, Key=key)
        break

# Delete the temporary folder (optional)
for obj in response.get('Contents', []):
    s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

print(f"Parquet file saved as s3://{bucket_name}/{final_output_key}")