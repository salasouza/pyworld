from pyspark.sql import SparkSession
import os

class readerFr:
    def __init__(self, path_folder=False, path_new_folder=False):
        self.path_folder = path_folder
        self.path_new_folder = path_new_folder

    def extraction(self):
        spark = SparkSession.builder.getOrCreate()
        path = self.path_folder
        csvPath = os.listdir(self.path_folder)
        os.makedirs(self.path_new_folder)

        for w in csvPath:
            filepath = '{}/{}'.format(path, w)
            df = spark.read.format('csv')\
                .option('header', 'true')\
                .load(filepath)
            df.write.save(self.path_new_folder,format="csv", mode="overwrite")
            df.show()

            # list = os.listdir('trust/')
            # number_files = len(list)
            # print(number_files)

        print('Sucess! Hour of Coffee!!!')

        print('Done test!')

object = readerFr('trust/','new_trust/')

object.extraction()
