CREATE TABLE home_temps (
`timestamp` STRING,
`dining_temp` DOUBLE,
`dining_hum` DOUBLE,
`outdoor_temp` DOUBLE,
`outdoor_hum` DOUBLE,
`bathroom_temp` DOUBLE,
`bathroom_hum` DOUBLE,
`bedroom_temp` DOUBLE,
`bedroom_hum` DOUBLE,)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
tblproperties("skip.header.line.count"="1");

-- I then loaded the data from the csv saved in HDFS into the table.
LOAD DATA INPATH '/home_data/home_data.csv' INTO TABLE home_temps;
