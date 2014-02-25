#!/usr/bin/python3
from pylab import *

# wavelength of laser
lam = 633e-6 # mm

# length from slit to screen
L = 23 # inches
L *= 25.4 # converting to mm

# distance from center to dark fringes for the smallest single slit
single_fringes = array([
  #m  distance (mm)
  [1, 7/2],
  [2, 13.5/2],
  [3, 20.5/2],
  [4, 28/2]
])

# distance from center to bright fringes for the second smallest double slit
double_fringes = array([
  #m  distance (mm)
  [1, 1],
  [2, 4.5/2],
  [3, 6.5/2],
  [4, 8.5/2],
  [5, 10.5/2]
])

b_tot = 0
for m, d in single_fringes:
  theta = arctan(d/L)
  b = m*lam/sin(theta)
  b_tot += b
  print('b:', b)

print()

a_tot = 0
for m, d in double_fringes:
  theta = arctan(d/L)
  a = m*lam/sin(theta)
  a_tot += a
  print('a:', a)

b_avg = b_tot/len(single_fringes)
a_avg = a_tot/len(double_fringes)

print('\na_avg:', a_avg)
print('b_avg:', b_avg)
print('a/b:', a_avg/b_avg)

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
