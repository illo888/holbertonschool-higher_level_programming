-- Lists all cities of California using subquery
-- Retrieves data without JOIN operation
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
