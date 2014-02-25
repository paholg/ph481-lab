#!/usr/bin/python3
from pylab import *

# wavelength of laser
lam = 633e-6 # mm

# length from slit to screen
L = 23 # inches
L *= 25.4 # converting to mm

# Distance from center to dark fringes for the smallest single slit. Distances
# were actaully meaasured from dark fringe to dark fringe, for greatest
# accuracy, and so are divided by 2.
single_fringes = array([
  #m  distance (mm)
  [1, 7/2],
  [2, 13.5/2],
  [3, 20.5/2],
  [4, 28/2]
])

# Distance from center to bright fringes for the second smallest double
# slit. Again, distances were measured from fringe to fringe and divided by 2.
double_fringes = array([
  #m  distance (mm)
  [1, 1],
  [2, 4.5/2],
  [3, 6.5/2],
  [4, 8.5/2],
  [5, 10.5/2]
])

b = zeros(len(single_fringes))
for (i, (m, d)) in enumerate(single_fringes):
  theta = arctan(d/L)
  b[i] = m*lam/sin(theta)
  print('b:', b[i])
print()

a = zeros(len(double_fringes))
for (i, (m, d)) in enumerate(double_fringes):
  theta = arctan(d/L)
  a[i] = m*lam/sin(theta)
  print('a:', a[i])

print('\na_avg: %g, std_dev: %g' %(a.mean(), a.std()))
print('b_avg: %g, std_dev: %g' %(b.mean(), b.std()))
print('a/b:', a.mean()/b.mean())

# directly measured slit spacing:
# focal length:
f = 25.4 # mm

# distance from object to lens:
do = 25.4 # mm

# distance from lens to image:
di = 22.5*25.4 # mm

# measured width:
w = 7.9 # mm

# magnification
M = di/do
a_meas = w/M

print('a (with lenses):', a_meas)
