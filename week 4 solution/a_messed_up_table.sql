--A messed up table
UPDATE Planet
SET kepler_name = null
WHERE status != 'CONFIRMED';

DELETE FROM Planet
WHERE radius < 0;

select * from Planet;
