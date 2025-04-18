-- Script to list all shows and their genres from the database hbtn_0d_tvshows
-- If a show doesn't have a genre, display NULL in the genre column
-- Results are sorted in ascending order by show title and genre name

SELECT 
    tv_shows.title,
    tv_genres.name
FROM 
    tv_shows
LEFT JOIN 
    tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN 
    tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY 
    tv_shows.title ASC, 
    tv_genres.name ASC;