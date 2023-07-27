-- Script that lists all shows from the database hbtn_0d_tvshows
-- that have at least one genre linked.

SELECT s.title, g.genre_id
FROM tv_shows AS s
INNER JOIN tv_show_genres AS g ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
