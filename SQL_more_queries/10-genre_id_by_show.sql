-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
USE hbtn_0d_tvshows;
SELECT * FROM
SELECT cities.id, cities.name, (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
