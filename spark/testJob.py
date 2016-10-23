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
#There are two ways to create RDDs:
# parallelizing an existing collection in your driver program,
# or referencing a dataset in an external storage system
textFile = sc.textFile("C:\codes\python_practice\spark\README.md")
count = textFile.count()
print count
linesWithSpark = textFile.filter(lambda line: "Spark" in line)
count2 = linesWithSpark.count()
print count2
count3 = textFile.map(lambda line: len(line.split())).reduce(lambda a, b: a if (a > b) else b)
print count3

# words = sc.parallelize(["scala","java","hadoop","spark","akka"])
# print(words.count())