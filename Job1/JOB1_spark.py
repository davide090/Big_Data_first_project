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

#dataframe2.printSchema()
#counts = text_file.flatMap(lambda line: line.split(",")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

#dataframe2.select('year').show()


year = dataframe2.withColumn('Time', from_unixtime('Time')).cache()
year = year.select(year.Time.substr(1,4).alias('Time'), 'Summary')


#parsed = parsed.withColumn('Summary', strip_punctuation(parsed.select('Summary')).lower()).cache
#summary = dataframe2.withColumn('Summary', regexp_replace('Summary','\p{Punct}', '')).cache().select('Summary')
year = year.withColumn('Summary', lower(dataframe2.Summary)).cache()
year = year.withColumn('Summary', regexp_replace(year.Summary,'\p{Punct}', ''))

year = year.select('Time', explode(split(col("Summary"), "\s+")).alias("Word"))
year = year.groupBy("Time", "Word").agg(count('Word').alias('Word_count'))
#year.sort('Time')
year = year.orderBy('Word_count', ascending=False)
#df.limit(10).withColumn('Wo', df.age + 2)

window = Window.partitionBy(year['Time']).orderBy(year['Word_count'].desc())

year = year.select('*', rank().over(window).alias('rank')).filter(col('rank') <= 10).select('Time', 'Word', 'Word_count').cache()
year.write.save('hdfs:///output/job1_spark.csv', format='csv', mode='overwrite')
#year.write.save('hdfs:///output/job1_spark.csv', format='csv', mode='overwrite')




print('Exec Time: ')
print(datetime.now() - startTime)
