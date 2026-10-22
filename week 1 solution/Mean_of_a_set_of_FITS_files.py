# Write your mean_fits function here:

import numpy as np
from astropy.io import fits

def mean_fits(L):
  M = []
  for image in (L):
    M.append(fits.open(image)[0].data)
  return np.mean(M, axis = 0)


if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
