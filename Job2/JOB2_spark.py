#!/usr/bin/python3

import datetime
from string import punctuation
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from datetime import datetime


startTime = datetime.now()

columns = ["Id","ProductId","UserId","ProfileName","HelpfulnessNumerator","HelpfulnessDenominator",
           "Score","Time","Summary","Text"]


#summary = strip_punctuation(words[8]).lower()
#year = datetime.datetime.fromtimestamp(int(words[7])).strftime('%Y'   

dataframe2 = spark.read.format('csv').option('header','true').option('mode','DROPMALFORMED')\
.load("hdfs:///user/hadoop/Reviews_4.csv")

product = dataframe2.withColumn('Time', from_unixtime('Time')).cache()
product = product.select('ProductId', product.Time.substr(1,4).alias('Time'), 'Score')
product = product.orderBy('ProductId')

#product.select(product.ProductId, product.Time.between(2003, 2013), product.Score).show()

product = product.filter(product.Time >= '2003').filter(product.Time <= '2012')
#product.show()


product = product.groupBy('ProductId', 'Time').agg(avg('Score').alias('avg_score'))

product = product.orderBy('ProductId','Time').cache()
product.write.save('hdfs:///output/job2_spark.csv', format='csv', mode='overwrite')

print('Exec Time: ')
print(datetime.now() - startTime)
