from pyspark.sql import SparkSession
from testjob.job import Job

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
job = Job(spark)
job.sparkVersion()

print(spark.version)