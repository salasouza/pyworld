from pyspark.sql import SparkSession
import os

def multiplereader():
    spark = SparkSession.builder.getOrCreate()
    path_folder = "trust/"
    csvPath = os.listdir(path_folder)
    for w in csvPath:
        filepath = '{}/{}'.format(path_folder, w)
        df = spark.read.format('csv')\
                .option('header','true')\
                .load(filepath)
        print('\nFile name is:', w)
        df.show()

object = multiplereader()
object
