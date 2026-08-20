CREATE TABLE performance (
`student_id` INT,
`age` INT,
`gender` STRING,
`school_type` STRING,
`parent_education` STRING,
`study_hours` STRING,
`attendance_percentage` STRING,
`internet_access` STRING,
`travel_time` STRING,
`extra_activities` STRING,
`study_method` STRING,
`math_score` STRING, 
`science_score` STRING, 
`english_score` STRING,
`overall_score` STRING,
`final_grade` STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
tblproperties("skip.header.line.count"="1");
