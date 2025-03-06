-- Use the second_table table to select the score and name of all players who have a name.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
