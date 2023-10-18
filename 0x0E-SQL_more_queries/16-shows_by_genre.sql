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
    tv_shows.title AS title,
    tv_genres.name AS name
    FROM tv_show_genres
    RIGHT JOIN tv_shows
    ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
    ORDER BY title, name;
