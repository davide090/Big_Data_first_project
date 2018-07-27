DROP TABLE Reviews;
DROP TABLE mapper_out;
DROP TABLE summary_words;
DROP TABLE year_word;
DROP TABLE year_word_count;
DROP TABLE result_1;


CREATE TABLE Reviews ( Id STRING, ProductId STRING, UserId STRING, ProfileName STRING, HelpfulnessNumerator STRING, HelpfulnessDenominator STRING,
         Score STRING, Time STRING, Summary STRING, Text STRING )

ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';

LOAD DATA LOCAL INPATH '/home/davide/Documenti/BIG_DATA/codice/Reviews_nofirstline.csv' INTO TABLE Reviews;

add jar /home/davide/Documenti/BIG_DATA/codice/unix_date.jar;

CREATE TEMPORARY FUNCTION get_year AS 'unix_date.Unix2Date';

SELECT Id, get_year(Time) FROM Reviews LIMIT 10;

--tabella anno, campo summary


--CREATE TABLE mapper_out AS
--SELECT regexp_replace(lower(r.Summary), "\!|\"|\,|\;|\-|\~|\:", "") as summary, get_year(r.Time) as year
--FROM Reviews as r;

--SELECT * FROM mapper_out LIMIT 100;

CREATE TABLE mapper_out AS
  ( SELECT get_year(r.Time) as year, regexp_replace(lower(r.Summary), "\!|\"|\,|\;|\-|\~|\:", "") as summary
	FROM Reviews as r);

CREATE TABLE year_word AS
SELECT mp.year, exp.splitted as word
FROM mapper_out mp
LATERAL VIEW explode(split(summary, ' ')) exp AS splitted;



CREATE TABLE year_word_count AS
SELECT year, word, count(1) as word_count
FROM year_word yw
WHERE year >= 1999
GROUP BY year, word;


CREATE TABLE result_1 AS
SELECT year, word, word_count 
FROM 
(SELECT year, word, word_count, 
       rank() over (partition by year order by word_count desc) as rank 
FROM year_word_count) t
WHERE rank <11;

--SELECT * FROM result_1;


DROP TABLE mapper_out;
DROP TABLE summary_words;
DROP TABLE year_word;
DROP TABLE year_word_count;










