-- MySQL server
-- should import the database dump from hbtn_0d_tvshows
-- should list all genres not linked to the show Dexter
-- should the tv_shows table contains only one record where title = Dexter
-- should each record should display: tv_genres.name
-- should results must be sorted in ascending order by the genre name
-- shoudl use a maximum of two SELECT statement
-- should name will be passed as an argument

SELECT tv_genres.name
    FROM tv_genres
    WHERE tv_genres.id NOT IN
    (SELECT tv_genres.id
    FROM tv_genres
    INNER JOIN tv_show_genres
    ON tv_genres.id = tv_show_genres.genre_id
    INNER JOIN tv_shows
    ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter")
ORDER BY tv_genres.name;
