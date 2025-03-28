-- Script to list all genres and the number of shows linked to each
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column: genre
-- Second column: number_of_shows
-- Results are sorted in descending order by the number of shows linked

SELECT 
    genres.name AS genre,
    COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM 
    genres
JOIN 
    tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY 
    genres.name
HAVING 
    number_of_shows > 0
ORDER BY 
    number_of_shows DESC;