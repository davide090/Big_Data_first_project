DROP TABLE Reviews;
DROP TABLE mapper_out;
DROP TABLE mapper_out_tmp;
DROP TABLE result_2;

CREATE TABLE Reviews ( Id STRING, ProductId STRING, UserId STRING, ProfileName STRING, HelpfulnessNumerator STRING, HelpfulnessDenominator STRING,
         Score STRING, Time STRING, Summary STRING, Text STRING )

ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INPATH 'Reviews_nofirstline.csv' INTO TABLE Reviews;

add jar unix_date.jar;

CREATE TEMPORARY FUNCTION get_year AS 'unix_date.Unix2Date';


CREATE TABLE mapper_out_tmp AS
SELECT ProductId as product, get_year(Time) as year, Score as score FROM Reviews;


CREATE TABLE mapper_out AS
SELECT * FROM mapper_out_tmp mp WHERE mp.year >= 2003 and mp.year <= 2012 ORDER BY product;


--SELECT * FROM mapper_out LIMIT 30;

CREATE TABLE result_2 AS
SELECT product, year, avg(score) FROM mapper_out GROUP BY product, year;



--SELECT * FROM result_2 LIMIT 100;

DROP TABLE mapper_out;
DROP TABLE mapper_out_tmp;
