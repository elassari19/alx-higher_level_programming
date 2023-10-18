-- MySQL server
-- should import the database dump from hbtn_0d_tvshows
-- should  lists all shows contained in hbtn_0d_tvshows
-- should should display: <TV Show genre> - <Number of shows linked to this genre>
-- should first column must be called genre
-- should second column must be called number_of_shows
-- shoudl not display a genre that doesn’t have any shows linked
-- should fesults sorted in descending order by the number of shows linked
-- should can use only one SELECT statement
-- should name will be passed as an argument

SELECT
    tv_genres.name AS genre,
    COUNT(tv_show_genres.genre_id) AS number_of_shows
    FROM tv_show_genres
    INNER JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
    GROUP BY genre
    ORDER BY number_of_shows DESC;
