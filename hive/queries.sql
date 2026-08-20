-- In my first querie, I listed the first ten rows of the HIVE table to show that the data loaded corectly.
SELECT * FROM performance LIMIT 10;

-- In my second querie, I counted the number of students in the table that had earned an 'f' as their overall final grade.
SELECT COUNT(*) FROM performance WHERE final_grade = 'f';
