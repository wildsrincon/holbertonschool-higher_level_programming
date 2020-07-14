-- List all genres and the number of shows linked to each
SELECT name AS 'genre', COUNT(*) AS number_shows
FROM tv_genres, tv_show_genres
WHERE tv_genres_id = tv_show_genres.genre_id
GROUP BY tv_genres.name 
ORDER BY number_shows DESC;
