# SQL Command Reference

| **Package/Method** | **Description** | **Code Example** |
|--------------------|------------------|------------------|
| `SELECT` | Retrieves data from one or more tables based on specified columns. | `SELECT column1, column2 FROM table_name;` |
| `FROM` | Specifies the table from which data is retrieved. | `SELECT column1, column2 FROM table_name;` |
| `WHERE` | Filters data based on specified conditions. | `SELECT column1, column2 FROM table_name WHERE condition;` |
| `ORDER BY` | Sorts the result set based on specified columns in ascending or descending order. | `SELECT column1, column2 FROM table_name ORDER BY column1 ASC;` |
| `GROUP BY` | Groups rows based on a specified column. | `SELECT column1, COUNT(*) FROM table_name GROUP BY column1;` |
| `HAVING` | Filters grouped data based on specified conditions. | `SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > 1;` |
| `INSERT INTO` | Inserts data into a table. | `INSERT INTO table_name (column1, column2) VALUES (value1, value2);` |
| `UPDATE` | Modifies data in a table based on specified conditions. | `UPDATE table_name SET column1 = value1 WHERE condition;` |
| `DELETE FROM` | Deletes data from a table based on specified conditions. | `DELETE FROM table_name WHERE condition;` |
| `CREATE TABLE` | Creates a new table with specified columns and data types. | `CREATE TABLE table_name (column1 INT, column2 VARCHAR(100));` |
| `ALTER TABLE` | Modifies the structure of an existing table. | `ALTER TABLE table_name ADD column3 DATE;` |
| `TRUNCATE TABLE` | Removes all records from a table without logging individual row deletions. | `TRUNCATE TABLE table_name;` |
| `DISTINCT` | Returns unique values from a column. | `SELECT DISTINCT column1 FROM table_name;` |
| `COUNT` | Counts the number of rows or non-null values in a column. | `SELECT COUNT(*) FROM table_name;` or `SELECT COUNT(column1) FROM table_name;` |
| `SUM` | Calculates the sum of values in a column. | `SELECT SUM(column1) FROM table_name;` |
| `AVG` | Calculates the average value of a column. | `SELECT AVG(column1) FROM table_name;` |
| `MAX` | Finds the maximum value in a column. | `SELECT MAX(column1) FROM table_name;` |
| `MIN` | Finds the minimum value in a column. | `SELECT MIN(column1) FROM table_name;` |
| `JOIN` | Combines rows from multiple tables based on related columns. | `SELECT column1, column2 FROM table1 JOIN table2 ON table1.column = table2.column;` |
| `INNER JOIN` | Returns only matching rows from both tables. | `SELECT column1, column2 FROM table1 INNER JOIN table2 ON table1.column = table2.column;` |
| `LEFT JOIN` | Returns all rows from the left table and matching rows from the right table. | `SELECT column1, column2 FROM table1 LEFT JOIN table2 ON table1.column = table2.column;` |
| `RIGHT JOIN` | Returns all rows from the right table and matching rows from the left table. | `SELECT column1, column2 FROM table1 RIGHT JOIN table2 ON table1.column = table2.column;` |
| `FULL JOIN` | Returns all rows from both tables, regardless of the match. | `SELECT column1, column2 FROM table1 FULL JOIN table2 ON table1.column = table2.column;` |
