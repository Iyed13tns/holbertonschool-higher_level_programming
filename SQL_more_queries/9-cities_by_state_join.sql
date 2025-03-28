-- Script to list all cities with their corresponding state names
-- Each record displays: cities.id - cities.name - states.name
-- Results are sorted in ascending order by cities.id

SELECT 
    cities.id, 
    cities.name, 
    states.name
FROM 
    cities
JOIN 
    states
ON 
    cities.state_id = states.id
ORDER BY 
    cities.id ASC;