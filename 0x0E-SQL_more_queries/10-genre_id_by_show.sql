-- MySQL server
-- should import the database dump from hbtn_0d_tvshows
-- should  lists all shows contained in hbtn_0d_tvshows
-- should should display: tv_shows.title - tv_show_genres.genre_id
-- should results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- should can use only one SELECT statement
-- should name will be passed as an argument

SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows INNER JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
    ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
