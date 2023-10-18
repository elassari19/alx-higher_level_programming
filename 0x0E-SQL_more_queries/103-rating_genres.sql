-- MySQL server
-- should import the database dump from hbtn_0d_tvshows_rate
-- should lists all shows from hbtn_0d_tvshows_rate by their rating
-- should each record should display: tv_shows.title - rating sum
-- should results must be sorted in ascending order by the rating
-- shoudl use a maximum of two SELECT statement
-- should name will be passed as an argument

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres
     ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
     ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings
     ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY rating DESC;
