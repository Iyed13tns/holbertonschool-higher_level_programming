-- This SQL query retrieves the count of each unique score from the `second_table`, grouping the results by score and ordering them in descending order based on the count.
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;