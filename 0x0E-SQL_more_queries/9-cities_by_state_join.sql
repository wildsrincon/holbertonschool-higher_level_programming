-- Lists all cities in database with cities id, name, and state name
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;
