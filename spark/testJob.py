'''if pycharm is not configured, the typical sample would be:'''
# import os
# import sys
#
# # Path for spark source folder
# os.environ['SPARK_HOME']="C:\mySoftware\spark-2.0.1-bin-hadoop2.7"
#
# # Append pyspark  to Python Path
# sys.path.append("C:\mySoftware\spark-2.0.1-bin-hadoop2.7\python")
# sys.path.append("C:\mySoftware\spark-2.0.1-bin-hadoop2.7\python\lib\py4j-0.10.3-src.zip")
#
# try:
#     from pyspark import SparkContext
#     from pyspark import SparkConf
#     print "Successfully imported Spark Modules"
# except ImportError as e:
#     print "Can not import Spark Modules", e
#     sys.exit(1)
#
# sc = SparkContext('local')
# words = sc.parallelize(["scala","java","hadoop","spark","akka"])
# print(words.count())

##################################################################
'''if pycharm is configured, the typical sample would be:'''
from pyspark import SparkContext

sc = SparkContext('local')
words = sc.parallelize(["scala","java","hadoop","spark","akka"])
print(words.count())