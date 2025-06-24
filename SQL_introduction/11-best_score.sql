-- This SQL query retrieves the scores and names from the `second_table` where the score is greater than or equal to 10, and orders the results in descending order based on the score.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;