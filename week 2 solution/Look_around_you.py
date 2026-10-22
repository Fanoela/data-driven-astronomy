# Write your find_closest function here
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

def angular_dist(ra1, dec1, ra2, dec2):
  ra1,dec1, ra2, dec2 = np.radians(ra1),np.radians(dec1), np.radians(ra2),np.radians(dec2)
  a = np.sin(np.abs(dec1 - dec2)/2)**2
  b = np.cos(dec1)*np.cos(dec2)*(np.sin(np.abs(ra2 - ra1)/2)**2)
  
  return np.degrees(2*np.arcsin(np.sqrt(a+b)))

cat = import_bss()

#print(np.array(cat))
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
  



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))

