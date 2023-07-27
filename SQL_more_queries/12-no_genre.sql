-- Script that lists all shows from the database hbtn_0d_tvshows
-- that do not have a genre linked.

SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g ON s.id = g.show_id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id;
