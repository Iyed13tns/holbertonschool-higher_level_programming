-- Script to list all genres of the show Dexter
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by the genre name

SELECT DISTINCT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;