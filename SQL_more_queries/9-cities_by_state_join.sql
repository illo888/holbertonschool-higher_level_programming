-- Lists all cities with their state names
-- Combines data using JOIN operation
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
