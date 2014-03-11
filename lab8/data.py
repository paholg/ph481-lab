#!/usr/bin/python3
from pylab import *

# part 1

# minimized intensity of reflected beam (zero intensity) by rotatin the QWP
# verified circular polarization by placing polaroid after QWP
#   - beam intensity was independent of polaroid angle
# found two positions each for circular polarization
# two positions which leave polarization unchanged


# part 2

# crystal splits text into two
# polaroid changes intensities of the copies of the text
#   - at some angle, only one copy of the text can be seen
#   - at 90 degrees to the first angle, only the other copy can be seen


# part 3

# light polarized orgthogonally to 141 degrees (at 51 degrees)
# initially 36.7 g of sugar in 200 mL of water

lam = 632.8 # nm
n_water = 1.33 # index of refraction of water
d_water = 6.4e-1 # dm; inner diameter of beaker
sugar_initial_mass = 36.7 # g

# amound ot sugar we add to water for each measureent
added_sugar = array([0, 20.2, 17.7, 20.1]) # g
# relative orientation of polaroid for zero transmission
orient = array([188, 190, 192, 193]) - 180 # degrees

water_volume = 200*ones(len(added_sugar)) # mL
sugar_density = 1.59 # g/mL

sugar_mass = sugar_initial_mass + zeros(len(added_sugar))
for i in range(len(sugar_mass)):
    sugar_mass[i] += sum(added_sugar[:i+1])

volume = water_volume + sugar_mass / sugar_density

a = orient / ( d_water * sugar_mass / volume )

print('Specific rotation for 632.8 nm light:','%.1f'%mean(a))
print('Varation:','%.1f'%std(a))
print('Specific rotation for 589 nm light:','%.1f'%(mean(a)*632.8/589))

