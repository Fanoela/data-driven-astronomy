# Write your crossmatch function here.
import numpy as np 
def hms2dec(h,m,s):
  return 15*(h + m/60 + s/3600)

def dms2dec(d,arcm,arcs):
  return (d/abs(d))*(abs(d) + arcm/60 + arcs/3600) 

def import_bss():
  res = []
  data = np.loadtxt('bss.dat', usecols=range(1, 7))
  for i, row in enumerate(data, 1):
    res.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
  return res

def import_super():
  data = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=(0, 1))
  res = []
  for i, row in enumerate(data, 1):
    res.append((i, row[0], row[1]))
  return res


def angular_dist(ra1, dec1, ra2, dec2):
  ra1,dec1, ra2, dec2 = np.radians(ra1),np.radians(dec1), np.radians(ra2),np.radians(dec2)
  a = np.sin(np.abs(dec1 - dec2)/2)**2
  b = np.cos(dec1)*np.cos(dec2)*(np.sin(np.abs(ra2 - ra1)/2)**2)
  
  return np.degrees(2*np.arcsin(np.sqrt(a+b)))

cat = import_bss()


def find_closest(cat, ra1,dec1):
  cat = np.array(cat)
  indice = cat[0,0]
  dist = angular_dist(ra1, dec1, cat[0,1], cat[0,2]) 
  
  for i in range(1,cat.shape[0]):  
    dist2 = angular_dist(ra1, dec1, cat[i,1], cat[i,2]) 
    if dist2 <= dist:
      dist = dist2
      indice = cat[i,0]
    else:
      pass
  return int(indice), dist

def distance(tuple_item):
  return tuple_item[2]

def crossmatch(bss_cat, super_cat, max_distance):
  bss_cat = np.array(bss_cat)
  super_cat = np.array(super_cat)
  matches = []
  no_matches = []
  id_match = []
  for i in range(bss_cat.shape[0]):
    for j in range(super_cat.shape[0]):
      d = angular_dist(bss_cat[i,1], bss_cat[i,2], super_cat[j,1], super_cat[j,2])
      if d <= max_distance:
        matches.append((int(bss_cat[i,0]), int(super_cat[j,0]), d))
        id_match.append(int(bss_cat[i,0]))
      else:
        pass
  id_match = set(id_match)
  no_matches = list(filter(lambda x: x not in id_match,bss_cat[:,0]))
  no_matches = [int(p) for p in no_matches]
  matches = [min(filter(lambda y: y[0]==p, matches), key = distance) for p in set(item[0] for item in matches)]
  return matches, no_matches


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))

