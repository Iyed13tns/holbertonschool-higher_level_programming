-- This SQL query selects the 'score' and 'name' columns from the 'second_table' where the 'name' is not NULL, and orders the results by 'score' in descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;