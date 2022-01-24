import unittest, os
from pyspark.sql import SparkSession
import impordatas as T

class readerFrTest(unittest.TestCase):

    def test_process(self):

        processor = T.readerFr("trust/")
        processor.extraction()

    # Check to quantify files



    
