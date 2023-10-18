-- MySQL server
-- should import the database dump from hbtn_0d_tvshows_rate
-- should lists all shows from hbtn_0d_tvshows_rate by their rating
-- should each record should display: tv_shows.title - rating sum
-- should results must be sorted in ascending order by the rating
-- shoudl use a maximum of two SELECT statement
-- should name will be passed as an argument

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
     ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
