--star coordinate
DELETE FROM Star;

ALTER TABLE Star
ADD COLUMN ra FLOAT, 
ADD COLUMN decl FLOAT ;

COPY Star (kepler_id, t_eff, radius, ra, decl)
from 'stars_full.csv' CSV;

\d Star
