-- In my first querie, I listed the first fifteen rows of the HIVE table to show that the data loaded corectly.
SELECT * FROM home_temps LIMIT 15;

-- In my second querie, I counted the number of hours in the table that the outside temperature was over 90 degrees.
SELECT COUNT(*) FROM home_temps WHERE outdoor_temp > 90;
