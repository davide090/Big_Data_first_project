DROP TABLE Reviews;
DROP TABLE mapper_out;
DROP TABLE result_3;

CREATE TABLE Reviews ( Id STRING, ProductId STRING, UserId STRING, ProfileName STRING, HelpfulnessNumerator STRING, HelpfulnessDenominator STRING,
         Score STRING, Time STRING, Summary STRING, Text STRING )

ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INPATH '/home/davide/Documenti/BIG_DATA/codice/Reviews_nofirstline.csv' INTO TABLE Reviews;

add jar /home/davide/Documenti/BIG_DATA/codice/unix_date.jar;

CREATE TEMPORARY FUNCTION get_year AS 'unix_date.Unix2Date';

CREATE TABLE mapper_out AS
SELECT ProductId as product, UserId as user_ FROM Reviews;


CREATE TABLE result_3 AS
SELECT
 t1.product AS item1,
 t2.product AS item2,
 COUNT(1) AS cnt
FROM
(
 SELECT DISTINCT product, user_
 FROM mapper_out
) t1
JOIN
(
 SELECT DISTINCT product, user_
 FROM mapper_out
) t2
ON (t1.user_ = t2.user_)
GROUP BY t1.product, t2.product
HAVING t1.product != t2.product
ORDER BY t1.product;


DROP TABLE mapper_out;




