# Apache Hive — Managed Table & SQL Validation

## Role in the Pipeline

Apache Hive provides the structured SQL layer between HDFS storage and the Spark MLlib workload. The project data loaded through NiFi into HDFS is used to create and populate a Hive managed table.

## Hive Table Design

**Table name:** `performance`

I created this table called performance with the column names the same as the original columns from the csv. 

## SQL Files

- [`create_tables.sql`](create_tables.sql) — table creation and data-loading SQL
- [`queries.sql`](queries.sql) — validation, exploration, and aggregation queries

## Data Load Verification

I viewed the first 10 rows of the Hive table in order to confirm that the data loaded properly into the table.

![Hive Load Results](screenshots/hive-load-results.png)

## Query & Aggregation Verification

I used an aggregation COUNT query to count the number of rows of the table where the overall final_grade was an f. Because Hive was able to identify those rows, it also confirms that the schema was set up correctly.

![Hive Query Results](screenshots/hive-query-results.png)

The validated Hive table becomes the structured input used by the PySpark MLlib application.
