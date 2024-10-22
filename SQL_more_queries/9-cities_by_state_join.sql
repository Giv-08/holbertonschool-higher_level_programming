-- lists all cities contained in the database hbtn_0d_usa
SELECT * FROM cities
WHERE state_id IN (SELECT id FROM states)
ORDER BY id ASC;
