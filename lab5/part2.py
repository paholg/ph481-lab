#!/usr/bin/python3
from pylab import *

# wavelength of laser
lam = 633e-6 # mm

# length from slit to screen
L = 23 # inches
L *= 25.4 # converting to mm

# distance from center to dark fringes for single slit (for the multi-slits)
single_fringes = array([
  #m  distance (mm)
  [1, 12/2],
  [2, 23.5/2],
  [3, 36/2]
])

# distance from center to bright fringes for 10 slits
multi_fringes = array([
  #m  distance (mm)
  [1, 6/2],
  [2, 11.5/2],
  [3, 17.5/2],
  [4, 23.5/2]
])

b_tot = 0
for m, d in single_fringes:
  theta = arctan(d/L)
  b = m*lam/sin(theta)
  b_tot += b
  print('b:', b)

print()

a_tot = 0
for m, d in multi_fringes:
  theta = arctan(d/L)
  a = m*lam/sin(theta)
  a_tot += a
  print('a:', a)

b_avg = b_tot/len(single_fringes)
a_avg = a_tot/len(multi_fringes)

print('\na_avg:', a_avg, 'mm')
print('b_avg:', b_avg, 'mm')
print('a/b:', a_avg/b_avg)

# diffraction grating
# distance from grating to wall
L = (212 + 65) # cm

# distance between dots on wall
d = (90 + 90.5)/2 # cm

theta = arctan(d/L)
a = 1*lam/sin(theta)

print('\na for diffraction grating:', a, 'mm')

# when the diffraction grating is rotated, the outer dots move away from the
# center, and change from dots to vertical narrow elipses / crescents

# new distance from grating to wall:
L = 212 + 42 # cm

# distance to ultraviolet from center dot:
d_uv = 53 # cm

# distance from ultraviolet to infrared:
d_between = 39 # cm

# distance to infrared:
d_ir = d_uv + d_between

theta_uv = arctan(d_uv/L)
theta_ir = arctan(d_ir/L)

lam_uv = a*sin(theta_uv)/1*1000000 # nm
lam_ir = a*sin(theta_ir)/1*1000000 # nm

print('\nwavelength uv:', lam_uv, 'nm')
print('wavelength ir:', lam_ir, 'nm')

# part 3
# distance from cd to wall
L = 212 + 39 # cm

# distance between dots
d = 124 # cm

theta = arctan(d/L)
a = 1*lam/sin(theta)

print('\na for cd:', a, 'mm')
