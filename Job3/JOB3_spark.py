#!/usr/bin/python3

import datetime
from string import punctuation
from pyspark.sql.functions import *
from pyspark.sql.window import Window
from datetime import datetime


startTime = datetime.now()

columns = ["Id","ProductId","UserId","ProfileName","HelpfulnessNumerator","HelpfulnessDenominator",
           "Score","Time","Summary","Text"]



dataframe2 = spark.read.format('csv').option('header','true').option('mode','DROPMALFORMED')\
.load("hdfs:///user/hadoop/Reviews_4.csv")

product1 = dataframe2.select(dataframe2.ProductId.alias('prod1'), dataframe2.UserId.alias('user1'))
product1 = product1.orderBy('prod1')

product2 = dataframe2.select(dataframe2.ProductId.alias('prod2'), dataframe2.UserId.alias('user2'))
product2 = product2.orderBy('prod2')

df = product1.join(product2, product1.user1 == product2.user2).filter(product1.prod1 != product2.prod2)\
    .orderBy(product1.prod1)
    
df = df.select(df.prod1.alias('Product1'), df.prod2.alias('Product2'), df.user1.alias('User'))

#df.show()



df.write.save('hdfs:///output/job3_spark.csv', format='csv', mode='overwrite')

print('Exec Time: ')
print(datetime.now() - startTime)
