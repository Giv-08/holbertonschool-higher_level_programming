-- Lists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;
SELECT * FROM states
WHERE id IN (SELECT state_id FROM cities);
