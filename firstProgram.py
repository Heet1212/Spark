from pyspark import SparkContext

sc = SparkContext("local", "FIRST PROGRSM")
rdd1 = sc.parallelize([1, 2, 3, 4])
print(rdd1.collect())
