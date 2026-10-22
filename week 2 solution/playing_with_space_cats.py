# Write your import_bss function here.
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
  
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Output of the import_bss and import_super functions
  bss_cat = import_bss()
  super_cat = import_super()
  print(bss_cat)
  print(super_cat)
