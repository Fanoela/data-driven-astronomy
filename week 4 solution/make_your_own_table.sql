--make your own table
CREATE TABLE Planet (

  kepler_id INTEGER not null,
  koi_name VARCHAR(15) unique not null ,
  kepler_name VARCHAR(15),
  status VARCHAR(20) not null,
  radius FLOAT not null
);

INSERT INTO Planet VALUES
(6862328, 'K00865.01', null, 'CANDIDATE', 119.021),
(10187017, 'K00082.05', 'Kepler-102 b', 'CONFIRMED', 5.286),
(10187017, 'K00082.04', 'Kepler-102 c', 'CONFIRMED', 7.071);

select * from Planet;
