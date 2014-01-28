from __future__ import division
from pylab import *

for i in xrange(1):
  data = loadtxt('scope_%i_1.csv' %i, delimiter=',', skiprows = 2)
  plot(data[:,0], data[:,1])
savetxt('bobos', data)
show()
print data
