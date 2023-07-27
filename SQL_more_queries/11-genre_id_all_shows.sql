-- Script that lists all shows from the database hbtn_0d_tvshows
-- along with their associated genre_id, including NULL for shows without a genre.

SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
