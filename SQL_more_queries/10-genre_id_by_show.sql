-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
USE hbtn_0d_tvshows;
SELECT cities.id, cities.name, states.name
WHERE states.id = cities.state_id
FROM cities
ORDER BY cities.id ASC;
