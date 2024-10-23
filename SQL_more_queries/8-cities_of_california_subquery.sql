-- Lists all the cities of California that can be found in the database hbtn_0d_usa
-- SELECT id INTO @california_id FROM states
-- WHERE name = 'California';
-- SELECT id, name FROM cities
-- WHERE state_id = @california_id
-- ORDER BY id ASC;

SELECT cities.id, cities.name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
