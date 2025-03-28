-- Script to list all genres and the number of shows linked to each
-- Each record displays: <TV Show genre> - <Number of shows linked to this genre>
-- First column: genre
-- Second column: number_of_shows
-- Results are sorted in descending order by the number of shows linked

SELECT 
    tv_genres.name AS genre,
    COUNT(tv_show_genres.show_id) AS number_of_shows
FROM 
    tv_genres
JOIN 
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY 
    tv_genres.name
ORDER BY 
    number_of_shows DESC;